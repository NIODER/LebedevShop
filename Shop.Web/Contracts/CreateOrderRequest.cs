namespace Shop.Web.Contracts;

public record CreateOrderRequest(
    string Address,
    string BasketId
);