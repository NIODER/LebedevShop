namespace Shop.Web.Entities;

public class Basket
{
    private readonly List<Item> items = [];

    public Guid BasketId { get; private set; }
    public IReadOnlyCollection<Item> Items => items.AsReadOnly();
    public decimal Total => items.Sum(i => i.Cost);

    private Basket(Guid guid, List<Item> items)
    {
        BasketId = guid;
        this.items = items;
    }

    private Basket(Guid guid)
    {
        BasketId = guid;
    }

    private Basket() { }

    public static Basket CreateEmpty() => new(Guid.NewGuid());

    public static Basket CreateFromItems(List<Item> items) => new(Guid.NewGuid(), items);

    public void AddItem(Item item)
    {
        items.Add(item);
    }

    public void RemoveItemById(Guid itemId)
    {
        items.RemoveAll(i => i.ItemId == itemId);
    }

    public void Clear()
    {
        items.Clear();
    }
}