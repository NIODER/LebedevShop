namespace Shop.Web.Entities;

public class Order
{
    public Guid OrderId { get; private set; }
    public string Address { get; private set; }
    public Basket Basket { get; private set; }

    private Order(Guid guid, string address, Basket basket)
    {
        OrderId = guid;
        Address = address;
        Basket = basket;
    }

#pragma warning disable CS8618 // for entity framework
    private Order() { }

    public static Order Create(string address, Basket basket) => new(Guid.NewGuid(), address, basket);
}