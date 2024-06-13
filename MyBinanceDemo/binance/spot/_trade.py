from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters


def new_order_test(self, symbol: str, side: str, type: str, **kwargs):
    """Test New Order (TRADE)

    Test new order creation and signature/recvWindow. Creates and validates a new order but does not send it into
    the matching engine.

    POST /api/v3/order/test

    https://binance-docs.github.io/apidocs/spot/en/#test-new-order-trade

    Args:
        symbol (str)
        side (str)
        type (str)
    Keyword Args:
        timeInForce (str, optional)
        quantity (float, optional)
        quoteOrderQty (float, optional)
        price (float, optional)
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT, or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/api/v3/order/test"
    return self.sign_request("POST", url_path, params)


def new_order(self, symbol: str, side: str, type: str, **kwargs):
    """New Order (TRADE)

    Post a new order

    POST /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#new-order-trade

    Args:
        symbol (str)
        side (str)
        type (str)
    Keyword Args:
        timeInForce (str, optional)
        quantity (float, optional)
        quoteOrderQty (float, optional)
        price (float, optional)
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        strategyId (int, optional)
        strategyType (int, optional): The value cannot be less than 1000000.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT, or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/api/v3/order"
    return self.sign_request("POST", url_path, params)


def cancel_order(self, symbol: str, **kwargs):
    """Cancel Order (TRADE)

    Cancel an active order.

    DELETE /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        newClientOrderId (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/order"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", url_path, payload)


def cancel_open_orders(self, symbol: str, **kwargs):
    """Cancel all Open Orders on a Symbol (TRADE)

    Cancels all active orders on a symbol.
    This includes OCO orders.

    DELETE api/v3/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#cancel-all-open-orders-on-a-symbol-trade

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/openOrders"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", url_path, payload)


def get_order(self, symbol, **kwargs):
    """Query Order (USER_DATA)

    Check an order's status.

    GET /api/v3/order

    https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/order"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def cancel_and_replace(
    self, symbol: str, side: str, type: str, cancelReplaceMode: str, **kwargs
):
    """Cancel an Existing Order and Send a New Order (USER_DATA)

    Cancels an existing order and places a new order on the same symbol.

    Filters are evaluated before the cancel order is placed.

    If the new order placement is successfully sent to the engine, the order count will increase by 1.

    Weight(IP): 1

    POST /api/v3/order/cancelReplace

    https://binance-docs.github.io/apidocs/spot/en/#cancel-an-existing-order-and-send-a-new-order-user_data

    Args:
        symbol (str)
        side (str)
        type (str)
        cancelReplaceMode (str)
    Keyword Args:
        timeInForce (str, optional): Order time in force
        quantity (float, optional): Order quantity
        quoteOrderQty (float, optional): Quote quantity
        price (float, optional): Order price
        cancelNewClientOrderId (str, optional): Used to uniquely identify this cancel. Automatically generated by default
        cancelOrigClientOrderId (str, optional): Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence.
        cancelOrderId (int, optional): Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence.
        newClientOrderId (str, optional): Used to identify the new order. Automatically generated by default
        strategyId (int, optional)
        strategyType (int, optional): The value cannot be less than 1000000.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        trailingDelta (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters(
        [
            [symbol, "symbol"],
            [side, "side"],
            [type, "type"],
            [cancelReplaceMode, "cancelReplaceMode"],
        ]
    )

    params = {
        "symbol": symbol,
        "side": side,
        "type": type,
        "cancelReplaceMode": cancelReplaceMode,
        **kwargs,
    }
    url_path = "/api/v3/order/cancelReplace"
    return self.sign_request("POST", url_path, params)


def get_open_orders(self, symbol=None, **kwargs):
    """Current Open Orders (USER_DATA)

    Get all open orders on a symbol.

    GET /api/v3/openOrders

    https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

    Args:
        symbol (str, optional)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/openOrders"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def get_orders(self, symbol: str, **kwargs):
    """All Orders (USER_DATA)

    Get all account orders; active, canceled, or filled.

    GET /api/v3/allOrders

    https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/allOrders"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def new_oco_order(
    self,
    symbol: str,
    side: str,
    quantity: float,
    price: float,
    stopPrice: float,
    **kwargs
):
    """New OCO (TRADE)

    Post a new oco order

    POST /api/v3/order/oco

    https://binance-docs.github.io/apidocs/spot/en/#new-oco-trade

    Args:
        symbol (str)
        side (str)
        quantity (float)
        price (float)
        stopPrice (float)
    Keyword Args:
        listClientOrderId (str, optional): A unique Id for the entire orderList
        limitClientOrderId (str, optional)
        limitStrategyId (int, optional)
        limitStrategyType (int, optional): The value cannot be less than 1000000.
        limitIcebergQty (float, optional)
        stopClientOrderId (str, optional)
        stopStrategyId (int, optional)
        stopStrategyType (int, optional): The value cannot be less than 1000000.
        stopLimitPrice (float, optional)
        stopIcebergQty (float, optional)
        stopLimitTimeInForce (str, optional)
        newOrderRespType (str, optional): Set the response JSON.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [symbol, "symbol"],
            [side, "side"],
            [quantity, "quantity"],
            [price, "price"],
            [stopPrice, "stopPrice"],
        ]
    )
    params = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "price": price,
        "stopPrice": stopPrice,
        **kwargs,
    }

    url_path = "/api/v3/order/oco"
    return self.sign_request("POST", url_path, params)


def cancel_oco_order(self, symbol, **kwargs):
    """Cancel OCO (TRADE)

    Cancel an entire Order List

    DELETE /api/v3/orderList

    https://binance-docs.github.io/apidocs/spot/en/#cancel-oco-trade

    Args:
        symbol (str)
    Keyword Args:
        orderListId (int, optional): Either orderListId or listClientOrderId must be provided
        listClientOrderId (str, optional): Either orderListId or listClientOrderId must be provided
        newClientOrderId (str, optional): Used to uniquely identify this cancel. Automatically generated by default.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/orderList"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", url_path, payload)


def get_oco_order(self, **kwargs):
    """Query OCO (USER_DATA)

    Retrieves a specific OCO based on provided optional parameters

    GET /api/v3/orderList

    https://binance-docs.github.io/apidocs/spot/en/#query-oco-user_data

    Keyword Args:
        orderListId (int, optional): Either orderListId or listClientOrderId must be provided
        origClientOrderId (str, optional): Either orderListId or listClientOrderId must be provided.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    url_path = "/api/v3/orderList"
    return self.sign_request("GET", url_path, {**kwargs})


def get_oco_orders(self, **kwargs):
    """Query all OCO (USER_DATA)

    Retrieves all OCO based on provided optional parameters

    GET /api/v3/allOrderList

    https://binance-docs.github.io/apidocs/spot/en/#query-all-oco-user_data

    Keyword Args:
        fromId (int, optional): If supplied, neither startTime or endTime can be provided
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default Value: 500; Max Value: 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/allOrderList"
    return self.sign_request("GET", url_path, {**kwargs})


def get_oco_open_orders(self, **kwargs):
    """Query Open OCO (USER_DATA)

    GET /api/v3/openOrderList

    https://binance-docs.github.io/apidocs/spot/en/#query-open-oco-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/openOrderList"
    return self.sign_request("GET", url_path, {**kwargs})


def account(self, **kwargs):
    """Account Information (USER_DATA)

    Get current account information

    GET /api/v3/account

    https://binance-docs.github.io/apidocs/spot/en/#account-information-user_data

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/account"
    return self.sign_request("GET", url_path, {**kwargs})


def my_trades(self, symbol: str, **kwargs):
    """Account Trade List (USER_DATA)

    Get trades for a specific account and symbol.

    GET /api/v3/myTrades

    https://binance-docs.github.io/apidocs/spot/en/#account-trade-list-user_data

    Args:
        symbol (str)
    Keyword Args:
        fromId (int, optional): TradeId to fetch from. Default gets most recent trades.
        orderId (int, optional): This can only be used in combination with symbol
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default Value: 500; Max Value: 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")

    url_path = "/api/v3/myTrades"
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", url_path, payload)


def get_order_rate_limit(self, **kwargs):
    """Query Current Order Count Usage (TRADE)

    Displays the user's current order count usage for all intervals.

    GET /api/v3/rateLimit/order

    https://binance-docs.github.io/apidocs/spot/en/#query-current-order-count-usage-trade

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/api/v3/rateLimit/order"
    return self.sign_request("GET", url_path, {**kwargs})


def query_prevented_matches(self, symbol: str, **kwargs):
    """Query Prevented Matches (USER_DATA)

    Displays the list of orders that were expired because of STP.

    For additional information on what a Prevented match is, as well as Self Trade Prevention (STP), please refer to our STP FAQ page.

    These are the combinations supported:

    * symbol + preventedMatchId
    * symbol + orderId
    * symbol + orderId + fromPreventedMatchId (limit will default to 500)
    * symbol + orderId + fromPreventedMatchId + limit

    Weight(IP):

    Case 	                          Weight
    If symbol is invalid: 	        2
    Querying by preventedMatchId: 	2
    Querying by orderId: 	          20

    GET /api/v3/myPreventedMatches

    https://binance-docs.github.io/apidocs/spot/en/#query-prevented-matches-user_data

    Args:
        symbol (str)
    Keyword Args:
        preventedMatchId (int, optional)
        orderId (int, optional): Order id
        fromPreventedMatchId (int, optional)
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    params = {"symbol": symbol, **kwargs}
    url_path = "/api/v3/myPreventedMatches"
    return self.sign_request("GET", url_path, params)


def query_allocations(self, symbol: str, **kwargs):
    """Query Cross-Collateral Information (USER_DATA)

    GET /api/v3/myAllocations

    https://binance-docs.github.io/apidocs/spot/en/#query-allocations-user_data

    Args:
        symbol (str)
    Keyword Args:
        startTime (int, optional)
        endTime (int, optional)
        fromAllocationId (int, optional)
        limit (int, optional): Default Value: 500; Max Value: 1000
        orderId (int, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    params = {"symbol": symbol, **kwargs}
    url_path = "/api/v3/myAllocations"
    return self.sign_request("GET", url_path, params)


def query_commission_rates(self, symbol: str, **kwargs):
    """Query Commission Rates (USER_DATA)

    GET /api/v3/account/commission

    https://binance-docs.github.io/apidocs/spot/en/#query-commission-rates-user_data

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")

    params = {"symbol": symbol, **kwargs}
    url_path = "/api/v3/account/commission"
    return self.sign_request("GET", url_path, params)
