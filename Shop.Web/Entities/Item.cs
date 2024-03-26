namespace Shop.Web.Entities;

public class Item
{
    public Guid ItemId { get; private set; }
    public string ItemName { get; private set; }
    public decimal Cost { get; private set; }
    public string Description { get; private set; }

    private Item(
        Guid guid,
        string itemName,
        string description,
        decimal cost)
    {
        ItemId = guid;
        ItemName = itemName;
        Cost = cost;
        Description = description;
    }

#pragma warning disable CS8618 // for entity framework
    private Item() { }

    public static Item Create(string itemName, string description, decimal cost) => 
        new(Guid.NewGuid(), itemName, description, cost);
}