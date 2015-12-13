ace.define("ace/mode/tradeblazer_highlight_rules", ["require", "exports", "module", "ace/lib/oop", "ace/mode/text_highlight_rules"], function (require, exports, module) {
    "use strict";

    var oop = require("../lib/oop");
    var TextHighlightRules = require("./text_highlight_rules").TextHighlightRules;

    var TradeblazerHighlightRules = function () {

        var keywords = (
            "A_AccountID|A_BrokerID|A_BuyAvgPrice|A_BuyPosition|A_BuyProfitLoss|A_CurrentEquity|A_DeleteOrder|A_FreeMargin|A_GetLastOpenOrderIndex|A_GetLastOrderIndex|A_GetOpenOrderCount|A_GetOrderCount|A_OpenOrderBuyOrSell|A_OpenOrderContractNo|A_OpenOrderEntryOrExit|A_OpenOrderFilledLot|A_OpenOrderFilledPrice|A_OpenOrderLot|A_OpenOrderPrice|A_OpenOrderStatus|A_OpenOrderTime|A_OrderBuyOrSell|A_OrderCanceledLot|A_OrderContractNo|A_OrderEntryOrExit|A_OrderFilledLot|A_OrderFilledPrice|A_OrderLot|A_OrderPrice|A_OrderStatus|A_OrderTime|A_PositionProfitLoss|A_PreviousEquity|A_ProfitLoss|A_SellAvgPrice|A_SellPosition|A_SellProfitLoss|A_SendOrder|A_TodayBuyPosition|A_TodayDeposit|A_TodayDrawing|A_TodaySellPosition|A_TotalAvgPrice|A_TotalFreeze|A_TotalMargin|A_TotalPosition|Abs|AccountDataExist|Acos|Acosh|Alert|AlertEnabled|Asin|Asinh|Atan2|Atan|Atanh|AvgBarsEvenTrade|AvgBarsLosTrade|AvgBarsWinTrade|AvgEntryPrice|BarCount|BarInterval|BarsSinceEntry|BarsSinceExit|BarsSinceLastEntry|BarStatus|BarType|BidAskSize|BigPointValue|Black|Blue|BoolArrayClear|BoolArrayCompare|BoolArrayCopy|BoolArrayEqual|BoolArrayErase|BoolArrayInsert|BoolArrayInsertRange|BoolArraySort|BoolArraySwap|Buy|BuyToCover|C|CanMarketOrder|CanShortTrade|CanStopOrder|CanTrade|Category|Ceiling|Close|Combin|Commentary|ContractProfit|ContractSize|ContractUnit|Cos|Cosh|Ctan|CurrencyName|CurrencySymbol|CurrentBar|CurrentContracts|CurrentDate|CurrentEntries|CurrentTime|Cyan|D|DarkBrown|DarkCyan|DarkGray|DarkGreen|DarkMagenta|DarkRed|DataCount|DataSourceSize|Date|DateAdd|DateDiff|DateTimeToString|DateToString|Day|DayFromDateTime|DefaultColor|EntryDate|EntryPrice|EntryTime|Enum_AmericanOption|Enum_Buy|Enum_CallOption|Enum_Canceled|Enum_Canceling|Enum_Declare|Enum_Declared|Enum_Deleted|Enum_Entry|Enum_EuropeanOption|Enum_Exit|Enum_ExitToday|Enum_Filled|Enum_FillPart|Enum_PutOption|Enum_Sell|Even|Exact|ExchangeName|ExitDate|ExitPrice|ExitTime|Exp|ExpiredDate|Fact|FileAppend|FileDelete|Floor|FormulaName|FracPart|Friday|GetBoolArraySize|GetGlobalVar2|GetGlobalVar|GetNumericArraySize|GetSessionCount|GetSessionEndTime|GetSessionStartTime|GetStringArraySize|GetTBProfileString2File|GetTBProfileString|GetUserID|Green|GrossLoss|GrossProfit|H|High|HistoryDataExist|Hour|HourFromDateTime|IIF|IIFString|InitialMargin|IntPart|InvalidInteger|InvalidNumeric|InvalidString|L|LargestLosTrade|LargestWinTrade|LastEntryDate|LastEntryPrice|LastEntryTime|Left|Len|LightGray|Ln|Log|Low|Lower|Magenta|MaintenanceMargin|MakeDate|MakeDateTime|MakeTime|MarginRatio|MarketPosition|MaxBarsBack|MaxConsecLosers|MaxConsecWinners|MaxContracts|MaxContractsHeld|MaxEntries|MaxPositionLoss|MaxPositionProfit|MaxSingleTradeSize|Mid|MilliSecond|MilliSecondFromDateTime|MinMove|Minute|MinuteFromDateTime|Mod|Monday|Month|MonthFromDateTime|Neg|NetProfit|NumericArrayClear|NumericArrayCompare|NumericArrayCopy|NumericArrayEqual|NumericArrayErase|NumericArrayInsert|NumericArrayInsertRange|NumericArraySort|NumericArraySwap|NumEvenTrades|NumLosTrades|NumWinTrades|O|Odd|Open|OpenInt|OptionStyle|OptionType|PercentProfit|Pi|PlayWavSound|PlotBool|PlotNumeric|PlotString|Portfolio_CurrentCapital|Portfolio_CurrentEntries|Portfolio_CurrentEquity|Portfolio_GrossLoss|Portfolio_GrossProfit|Portfolio_InitCapital|Portfolio_MaxDrawDown|Portfolio_MaxDrawDownRatio|Portfolio_NetProfit|Portfolio_NumLossTrades|Portfolio_NumWinTrades|Portfolio_PercentProfit|Portfolio_PositionProfit|Portfolio_TotalProfit|Portfolio_TotalTrades|Portfolio_UsedMargin|PositionProfit|Power|PriceScale|Q_AskPrice|Q_AskPriceFlag|Q_AskVol|Q_AvgPrice|Q_BidPrice|Q_BidPriceFlag|Q_BidVol|Q_Close|Q_High|Q_HisHigh|Q_HisLow|Q_InsideVol|Q_Last|Q_LastDate|Q_LastFlag|Q_LastTime|Q_LastVol|Q_Low|Q_LowerLimit|Q_Open|Q_OpenInt|Q_OpenIntFlag|Q_Oscillation|Q_OutsideVol|Q_PreOpenInt|Q_PreSettlePrice|Q_PriceChg|Q_PriceChgRatio|Q_TickChg|Q_TodayEntryVol|Q_TodayExitVol|Q_TotalVol|Q_TurnOver|Q_UpperLimit|QuoteDataExist|Rand|Red|RelativeSymbol|Rgb|Right|Round|RoundDown|RoundUp|Saturday|Second|SecondFromDateTime|Sell|SellShort|SetBoolArraySize|SetGlobalVar2|SetGlobalVar|SetNumericArraySize|SetStringArraySize|SetTBProfileString2File|SetTBProfileString|Sign|Sin|Sinh|Sqr|Sqrt|StrikePrice|StringArrayClear|StringArrayCompare|StringArrayCopy|StringArrayEqual|StringArrayErase|StringArrayInsert|StringArrayInsertRange|StringArraySort|StringArraySwap|StringToDate|StringToDateTime|StringToTime|Sunday|Symbol|SymbolName|SymbolType|SystemDateTime|T|Tan|Tanh|Text|Thursday|Time|TimeDiff|TimeToString|TotalBarsEvenTrades|TotalBarsLosTrades|TotalBarsWinTrades|TotalTrades|TradingDayLeft|Trim|Tuesday|Unplot|Upper|V|Value|Vol|Wednesday|Weekday|WeekdayFromDateTime|White|Year|YearFromDateTime|Yellow"
        );

        var builtinConstants = (
            "true|false"
        );

        var builtinFunctions = (
            "avg|count|first|last|max|min|sum|ucase|lcase|mid|len|round|rank|now|format|" +
            "coalesce|ifnull|isnull|nvl"
        );

        var dataTypes = (
            "int|numeric|decimal|date|varchar|char|bigint|float|double|bit|binary|text|set|timestamp|" +
            "money|real|number|integer"
        );

        var keywordMapper = this.createKeywordMapper({
            "support.function": builtinFunctions,
            "keyword": keywords,
            "constant.language": builtinConstants,
            "storage.type": dataTypes
        }, "identifier", true);

        this.$rules = {
            "start": [{
                token: "comment",
                regex: "//.*$"
            }, {
                token: "comment",
                start: "/\\*",
                end: "\\*/"
            }, {
                token: "string",           // " string
                regex: '".*?"'
            }, {
                token: "string",           // ' string
                regex: "'.*?'"
            }, {
                token: "constant.numeric", // float
                regex: "[+-]?\\d+(?:(?:\\.\\d*)?(?:[eE][+-]?\\d+)?)?\\b"
            }, {
                token: keywordMapper,
                regex: "[a-zA-Z_$][a-zA-Z0-9_$]*\\b"
            }, {
                token: "keyword.operator",
                regex: "\\+|\\-|\\/|\\/\\/|%|<@>|@>|<@|&|\\^|~|<|>|<=|=>|==|!=|<>|="
            }, {
                token: "paren.lparen",
                regex: "[\\(]"
            }, {
                token: "paren.rparen",
                regex: "[\\)]"
            }, {
                token: "text",
                regex: "\\s+"
            }]
        };
        this.normalizeRules();
    };

    oop.inherits(TradeblazerHighlightRules, TextHighlightRules);

    exports.TradeblazerHighlightRules = TradeblazerHighlightRules;
});



ace.define("ace/mode/tradeblazer", ["require", "exports", "module", "ace/lib/oop", "ace/mode/text", "ace/mode/tradeblazer_highlight_rules", "ace/range"], function (require, exports, module) {
    "use strict";

    var oop = require("../lib/oop");
    var TextMode = require("./text").Mode;
    var TradeblazerHighlightRules = require("./tradeblazer_highlight_rules").TradeblazerHighlightRules;
    var Range = require("../range").Range;

    var Mode = function () {
        this.HighlightRules = TradeblazerHighlightRules;
    };
    oop.inherits(Mode, TextMode);

    (function () {
        this.lineCommentStart = "//";

        this.$id = "ace/mode/tradeblazer";
    }).call(Mode.prototype);

    exports.Mode = Mode;
});
