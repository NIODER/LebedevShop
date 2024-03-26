using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Shop.Web.Entities;

namespace Shop.Web.Persistance.Configurations;

public class OrdersConfiguration : IEntityTypeConfiguration<Order>
{
    public void Configure(EntityTypeBuilder<Order> builder)
    {
        builder.ToTable("Orders");
        builder.HasKey(o => o.OrderId);
        builder.Property(o => o.OrderId)
            .IsRequired()
            .ValueGeneratedNever();

        builder.Property(o => o.Address)
            .HasMaxLength(256)
            .IsRequired();

        builder.HasOne(o => o.Basket)
            .WithMany();
    }
}