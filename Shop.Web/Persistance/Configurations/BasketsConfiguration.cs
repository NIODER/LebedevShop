using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Shop.Web.Entities;

namespace Shop.Web.Persistance.Configurations;

public class BasketsConfiguration : IEntityTypeConfiguration<Basket>
{
    public void Configure(EntityTypeBuilder<Basket> builder)
    {
        builder.ToTable("Baskets");
        builder.HasKey(b => b.BasketId);
        builder.Property(b => b.BasketId)
            .IsRequired()
            .ValueGeneratedNever();

        builder.Ignore(b => b.Total);

        builder.HasMany(b => b.Items)
            .WithMany();
    }
}
