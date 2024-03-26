using Microsoft.EntityFrameworkCore;

namespace Shop.Web.Persistance;

public sealed class ShopDbContextFactory(IConfiguration configuration) : IDbContextFactory<ShopDbContext>
{
    public const string DB_CONNECTIONS_STIRNGS_SECTION_NAME = "DbConnectionStrings";
    private readonly List<string> _connecitonStrings = configuration
            .GetRequiredSection(DB_CONNECTIONS_STIRNGS_SECTION_NAME)
            .Get<List<string>>()
                ?? throw new("No db connection strings was found in configuration");
    private static int currentConnectionString = 0;

    public ShopDbContext CreateDbContext()
    {
        var context = CreateContext(_connecitonStrings[currentConnectionString]);
        currentConnectionString = (currentConnectionString + 1) % _connecitonStrings.Count;
        return context;
    }

    public async Task EnsureDatabasesCreated()
    {
        foreach (var connectionString in _connecitonStrings)
        {
            await CreateContext(connectionString).Database.EnsureCreatedAsync();
        }
    }

    private static ShopDbContext CreateContext(string connectionString)
    {
        var options = new DbContextOptionsBuilder().UseNpgsql(connectionString).Options;
        return new ShopDbContext(options);
    }

    public void AddConnectionString(string connectionString)
    {
        _connecitonStrings.Add(connectionString);
    }

    public void RemoveConnectionString(string connectionString)
    {
        _connecitonStrings.Remove(connectionString);
    }

    public void RemoveConnectionStringByIndex(int index)
    {
        _connecitonStrings.RemoveAt(index);
    }

    public void Clear()
    {
        _connecitonStrings.Clear();
    }
}
