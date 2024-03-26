using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Shop.Web.Entities;

namespace Shop.Web.Persistance.Configurations;

public class ItemsConfiguration : IEntityTypeConfiguration<Item>
{
    public void Configure(EntityTypeBuilder<Item> builder)
    {
        builder.ToTable("Items");
        builder.HasKey(i => i.ItemId);
        builder.Property(i => i.ItemId)
            .IsRequired()
            .ValueGeneratedNever();

        builder.Property(i => i.ItemName)
            .HasMaxLength(100)
            .IsRequired();

        builder.Property(i => i.Description)
            .HasMaxLength(500)
            .IsRequired();
        
        builder.Property(i => i.Cost)
            .IsRequired();
    }
}