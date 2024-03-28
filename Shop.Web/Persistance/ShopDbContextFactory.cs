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
        List<string> failedConnectionStrings = [];
        foreach (var connectionString in _connecitonStrings)
        {
            try
            {
                await CreateContext(connectionString).Database.EnsureCreatedAsync();
            }
            catch(Exception e)
            {
                Console.WriteLine("Failed to create database");
                Console.WriteLine("Error message:");
                Console.WriteLine(e);
                failedConnectionStrings.Add(connectionString);
            }
        }
        while (failedConnectionStrings.Count != 0)
        {
            for (int i = 0; i < failedConnectionStrings.Count; i++)
            {
                try
                {
                    await CreateContext(failedConnectionStrings[i]).Database.EnsureCreatedAsync();
                    failedConnectionStrings.RemoveAt(i);
                    i--;
                }
                catch(Exception)
                {
                    Console.WriteLine("Failed to create database");
                    continue;
                }
            }
            Console.WriteLine("Retrying in 3 seconds");
            await Task.Delay(3000);
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
