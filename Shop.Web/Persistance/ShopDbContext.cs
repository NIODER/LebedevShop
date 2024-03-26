using System.Reflection;
using Microsoft.EntityFrameworkCore;
using Shop.Web.Entities;

namespace Shop.Web.Persistance;

public class ShopDbContext(DbContextOptions options) : DbContext(options)
{
    public DbSet<Order> Orders { get; private set; }
    public DbSet<Item> Items { get; private set; }
    public DbSet<Basket> Baskets { get; private set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfigurationsFromAssembly(Assembly.GetExecutingAssembly());
        base.OnModelCreating(modelBuilder);
    }
}