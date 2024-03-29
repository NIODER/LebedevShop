using System.Text.Json;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Shop.Web.Contracts;
using Shop.Web.Entities;
using Shop.Web.Persistance;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddDbContextFactory<ShopDbContext, ShopDbContextFactory>();
builder.Services.AddScoped(opt => opt.GetRequiredService<IDbContextFactory<ShopDbContext>>().CreateDbContext());

var app = builder.Build();

var dbCreations = new ShopDbContextFactory(app.Configuration).EnsureDatabasesCreated();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.MapGet("/items", (ShopDbContext context) =>
{
    return context.Items.ToList();
});

app.MapGet("/items/{id}", (ShopDbContext context, Guid id) =>
{
    var item = context.Items.SingleOrDefault(i => i.ItemId == id);
    return item;
});

app.MapPut("/items", (ShopDbContext context, [FromBody]CreateItemRequest item) =>
{
    var createdItem = context.Items.Add(Item.Create(item.ItemName, item.Description, item.Cost)).Entity;
    context.SaveChanges();
    return createdItem;
});

app.MapDelete("/items/{id}", (ShopDbContext context, Guid id) =>
{
    var item = context.Items.SingleOrDefault(i => i.ItemId == id) ?? throw new ArgumentException($"No item with id {id} found.");
    context.Items.Remove(item);
    context.SaveChanges();
    return item;
});

app.MapGet("/basket/{id}", (ShopDbContext context, Guid id) =>
{
    return context.Baskets
        .Include(b => b.Items)
        .SingleOrDefault(b => b.BasketId == id);
});

app.MapPost("/basket/{basketId}/{itemId}", (ShopDbContext context, Guid basketId, Guid itemId) => 
{
    var basket = context.Baskets
        .Include(b => b.Items)
        .SingleOrDefault(b => b.BasketId == basketId) ?? throw new ArgumentException($"No basket with id {basketId} found.");
    var item = context.Items.SingleOrDefault(i => i.ItemId == itemId) ?? throw new ArgumentException($"No item with id {itemId} found.");
    basket.AddItem(item);
    context.Baskets.Update(basket);
    context.SaveChanges();
    return basket;
});

app.MapPut("/basket", (ShopDbContext context) =>
{
    var basket = context.Baskets.Add(Basket.CreateEmpty()).Entity;
    context.SaveChanges();
    return basket;
});

app.MapDelete("/basket/{basketId}/{itemId}", (ShopDbContext context, Guid basketId, Guid itemId) =>
{
    var basket = context.Baskets
        .Include(b => b.Items)
        .SingleOrDefault(b => b.BasketId == basketId) ?? throw new ArgumentException($"No basket with id {basketId} found.");
    basket.RemoveItemById(itemId);
    context.Baskets.Update(basket);
    context.SaveChanges();
    return basket;
});

app.MapDelete("/basket/{id}", (ShopDbContext context, Guid id) =>
{
    var basket = context.Baskets
        .Include(b => b.Items)
        .SingleOrDefault(b => b.BasketId == id) ?? throw new ArgumentException($"No basket with id {id} found.");
    context.Remove(basket);
    context.SaveChanges();
    return basket;
});

app.MapPut("/order", (ShopDbContext context, [FromBody]CreateOrderRequest request) =>
{
    var basket = context.Baskets
        .Include(b => b.Items)
        .SingleOrDefault(b => b.BasketId == Guid.Parse(request.BasketId)) ?? throw new ArgumentException($"No basket with id {request.BasketId} found.");
    var order = context.Orders.Add(Order.Create(request.Address, basket)).Entity;
    context.SaveChanges();
    return order;
});

app.MapGet("/order/{id}", (ShopDbContext context, Guid id) =>
{
    return context.Orders.SingleOrDefault(o => o.OrderId == id) 
        ?? throw new ArgumentException($"No order with id {id} was found.");
});

await dbCreations;

app.Run();
