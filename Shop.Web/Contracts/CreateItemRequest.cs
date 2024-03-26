namespace Shop.Web.Contracts;

public record CreateItemRequest(
    string ItemName,
    string Description,
    decimal Cost
);