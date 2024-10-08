
# ----------------------
# Generated file
# 2023-08-08 09:09:30.634904
# ----------------------
from tvscreener.field import Field


class StockField(Field):
    ALL_TIME_HIGH = 'All Time High', 'High.All', 'round', False, False
    ALL_TIME_LOW = 'All Time Low', 'Low.All', 'round', False, False
    ALL_TIME_PERFORMANCE = 'All Time Performance', 'Perf.All', 'percent', False, False
    AROON_DOWN_14 = 'Aroon Down (14)', 'Aroon.Down', 'round', True, False
    AROON_UP_14 = 'Aroon Up (14)', 'Aroon.Up', 'round', True, False
    AVERAGE_DAY_RANGE_14 = 'Average Day Range (14)', 'ADR', 'float', True, False
    AVERAGE_DIRECTIONAL_INDEX_14 = 'Average Directional Index (14)', 'ADX', 'computed_recommendation', True, False
    AVERAGE_TRUE_RANGE_14 = 'Average True Range (14)', 'ATR', 'float', True, False
    AVERAGE_VOLUME_10_DAY = 'Average Volume (10 day)', 'average_volume_10d_calc', 'number_group', False, False
    AVERAGE_VOLUME_30_DAY = 'Average Volume (30 day)', 'average_volume_30d_calc', 'number_group', False, False
    AVERAGE_VOLUME_60_DAY = 'Average Volume (60 day)', 'average_volume_60d_calc', 'number_group', False, False
    AVERAGE_VOLUME_90_DAY = 'Average Volume (90 day)', 'average_volume_90d_calc', 'number_group', False, False
    AWESOME_OSCILLATOR = 'Awesome Oscillator', 'AO', 'computed_recommendation', True, True
    BASIC_EPS_FY = 'Basic EPS (FY)', 'basic_eps_net_income', 'currency', False, False
    BASIC_EPS_TTM = 'Basic EPS (TTM)', 'earnings_per_share_basic_ttm', 'currency', False, False
    BOLLINGER_LOWER_BAND_20 = 'Bollinger Lower Band (20)', 'BB.lower', 'computed_recommendation', True, False
    BOLLINGER_UPPER_BAND_20 = 'Bollinger Upper Band (20)', 'BB.upper', 'computed_recommendation', True, False
    BULL_BEAR_POWER = 'Bull Bear Power', 'BBPower', 'recommendation', True, False
    CANDLE_3BLACKCROWS = 'Candle.3BlackCrows', 'Candle.3BlackCrows', 'bool', True, False
    CANDLE_3WHITESOLDIERS = 'Candle.3WhiteSoldiers', 'Candle.3WhiteSoldiers', 'bool', True, False
    CANDLE_ABANDONEDBABY_BEARISH = 'Candle.AbandonedBaby.Bearish', 'Candle.AbandonedBaby.Bearish', 'bool', True, False
    CANDLE_ABANDONEDBABY_BULLISH = 'Candle.AbandonedBaby.Bullish', 'Candle.AbandonedBaby.Bullish', 'bool', True, False
    CANDLE_DOJI = 'Candle.Doji', 'Candle.Doji', 'bool', True, False
    CANDLE_DOJI_DRAGONFLY = 'Candle.Doji.Dragonfly', 'Candle.Doji.Dragonfly', 'bool', True, False
    CANDLE_DOJI_GRAVESTONE = 'Candle.Doji.Gravestone', 'Candle.Doji.Gravestone', 'bool', True, False
    CANDLE_ENGULFING_BEARISH = 'Candle.Engulfing.Bearish', 'Candle.Engulfing.Bearish', 'bool', True, False
    CANDLE_ENGULFING_BULLISH = 'Candle.Engulfing.Bullish', 'Candle.Engulfing.Bullish', 'bool', True, False
    CANDLE_EVENINGSTAR = 'Candle.EveningStar', 'Candle.EveningStar', 'bool', True, False
    CANDLE_HAMMER = 'Candle.Hammer', 'Candle.Hammer', 'bool', True, False
    CANDLE_HANGINGMAN = 'Candle.HangingMan', 'Candle.HangingMan', 'bool', True, False
    CANDLE_HARAMI_BEARISH = 'Candle.Harami.Bearish', 'Candle.Harami.Bearish', 'bool', True, False
    CANDLE_HARAMI_BULLISH = 'Candle.Harami.Bullish', 'Candle.Harami.Bullish', 'bool', True, False
    CANDLE_INVERTEDHAMMER = 'Candle.InvertedHammer', 'Candle.InvertedHammer', 'bool', True, False
    CANDLE_KICKING_BEARISH = 'Candle.Kicking.Bearish', 'Candle.Kicking.Bearish', 'bool', True, False
    CANDLE_KICKING_BULLISH = 'Candle.Kicking.Bullish', 'Candle.Kicking.Bullish', 'bool', True, False
    CANDLE_LONGSHADOW_LOWER = 'Candle.LongShadow.Lower', 'Candle.LongShadow.Lower', 'bool', True, False
    CANDLE_LONGSHADOW_UPPER = 'Candle.LongShadow.Upper', 'Candle.LongShadow.Upper', 'bool', True, False
    CANDLE_MARUBOZU_BLACK = 'Candle.Marubozu.Black', 'Candle.Marubozu.Black', 'bool', True, False
    CANDLE_MARUBOZU_WHITE = 'Candle.Marubozu.White', 'Candle.Marubozu.White', 'bool', True, False
    CANDLE_MORNINGSTAR = 'Candle.MorningStar', 'Candle.MorningStar', 'bool', True, False
    CANDLE_SHOOTINGSTAR = 'Candle.ShootingStar', 'Candle.ShootingStar', 'bool', True, False
    CANDLE_SPINNINGTOP_BLACK = 'Candle.SpinningTop.Black', 'Candle.SpinningTop.Black', 'bool', True, False
    CANDLE_SPINNINGTOP_WHITE = 'Candle.SpinningTop.White', 'Candle.SpinningTop.White', 'bool', True, False
    CANDLE_TRISTAR_BEARISH = 'Candle.TriStar.Bearish', 'Candle.TriStar.Bearish', 'bool', True, False
    CANDLE_TRISTAR_BULLISH = 'Candle.TriStar.Bullish', 'Candle.TriStar.Bullish', 'bool', True, False
    CASH_AND_EQUIVALENTS_FY = 'Cash & Equivalents (FY)', 'cash_n_equivalents_fy', 'currency', False, False
    CASH_AND_EQUIVALENTS_MRQ = 'Cash & Equivalents (MRQ)', 'cash_n_equivalents_fq', 'currency', False, False
    CASH_AND_SHORT_TERM_INVESTMENTS_FY = 'Cash and short term investments (FY)', 'cash_n_short_term_invest_fy', 'currency', False, False
    CASH_AND_SHORT_TERM_INVESTMENTS_MRQ = 'Cash and short term investments (MRQ)', 'cash_n_short_term_invest_fq', 'currency', False, False
    CHAIKIN_MONEY_FLOW_20 = 'Chaikin Money Flow (20)', 'ChaikinMoneyFlow', 'round', False, False
    CHANGE = 'Change', 'change_abs', 'currency', True, False
    CHANGE_15MIN = 'Change 15m', 'change_abs.15', 'float', False, False
    CHANGE_15MIN_PERCENT = 'Change 15m, %', 'change.15', 'percent', False, False
    CHANGE_1H = 'Change 1h', 'change_abs.60', 'round', False, False
    CHANGE_1H_PERCENT = 'Change 1h, %', 'change.60', 'percent', False, False
    CHANGE_1MIN = 'Change 1m', 'change_abs.1', 'float', False, False
    CHANGE_1M = 'Change 1M', 'change_abs.1M', 'round', False, False
    CHANGE_1MIN_PERCENT = 'Change 1m, %', 'change.1', 'percent', False, False
    CHANGE_1M_PERCENT = 'Change 1M, %', 'change.1M', 'percent', False, False
    CHANGE_1W = 'Change 1W', 'change_abs.1W', 'round', False, False
    CHANGE_1W_PERCENT = 'Change 1W, %', 'change.1W', 'percent', False, False
    CHANGE_4H = 'Change 4h', 'change_abs.240', 'round', False, False
    CHANGE_4H_PERCENT = 'Change 4h, %', 'change.240', 'percent', False, False
    CHANGE_5MIN = 'Change 5m', 'change_abs.5', 'round', False, False
    CHANGE_5MIN_PERCENT = 'Change 5m, %', 'change.5', 'percent', False, False
    CHANGE_FROM_OPEN = 'Change from Open', 'change_from_open_abs', 'currency', True, False
    CHANGE_FROM_OPEN_PERCENT = 'Change from Open %', 'change_from_open', 'percent', True, False
    CHANGE_PERCENT = 'Change %', 'change', 'percent', True, False
    COMMODITY_CHANNEL_INDEX_20 = 'Commodity Channel Index (20)', 'CCI20', 'computed_recommendation', True, True
    COUNTRY = 'Country', 'country', 'text', False, False
    CURRENCY = 'Currency', 'currency', 'text', False, False
    CURRENT_RATIO_MRQ = 'Current Ratio (MRQ)', 'current_ratio', 'round', False, False
    DEBT_TO_EQUITY_RATIO_MRQ = 'Debt to Equity Ratio (MRQ)', 'debt_to_equity', 'round', False, False
    DESCRIPTION = 'Description', 'description', 'text', False, False
    DIVIDENDS_PAID_FY = 'Dividends Paid (FY)', 'dividends_paid', 'currency', False, False
    DIVIDENDS_PER_SHARE_ANNUAL_YOY_GROWTH = 'Dividends per share (Annual YoY Growth)', 'dps_common_stock_prim_issue_yoy_growth_fy', 'percent', False, False
    DIVIDENDS_PER_SHARE_FY = 'Dividends per Share (FY)', 'dps_common_stock_prim_issue_fy', 'currency', False, False
    DIVIDENDS_PER_SHARE_MRQ = 'Dividends per Share (MRQ)', 'dividends_per_share_fq', 'currency', False, False
    DIVIDEND_YIELD_FORWARD = 'Dividend Yield Forward', 'dividend_yield_recent', 'percent', False, False
    DONCHIAN_CHANNELS_LOWER_BAND_20 = 'Donchian Channels Lower Band (20)', 'DonchCh20.Lower', 'round', True, False
    DONCHIAN_CHANNELS_UPPER_BAND_20 = 'Donchian Channels Upper Band (20)', 'DonchCh20.Upper', 'round', True, False
    EBITDA_ANNUAL_YOY_GROWTH = 'EBITDA (Annual YoY Growth)', 'ebitda_yoy_growth_fy', 'percent', False, False
    EBITDA_QUARTERLY_QOQ_GROWTH = 'EBITDA (Quarterly QoQ Growth)', 'ebitda_qoq_growth_fq', 'percent', False, False
    EBITDA_QUARTERLY_YOY_GROWTH = 'EBITDA (Quarterly YoY Growth)', 'ebitda_yoy_growth_fq', 'percent', False, False
    EBITDA_TTM = 'EBITDA (TTM)', 'ebitda', 'currency', False, False
    EBITDA_TTM_YOY_GROWTH = 'EBITDA (TTM YoY Growth)', 'ebitda_yoy_growth_ttm', 'percent', False, False
    ENTERPRISE_VALUEEBITDA_TTM = 'Enterprise Value/EBITDA (TTM)', 'enterprise_value_ebitda_ttm', 'round', False, False
    ENTERPRISE_VALUE_MRQ = 'Enterprise Value (MRQ)', 'enterprise_value_fq', 'currency', False, False
    EPS_DILUTED_ANNUAL_YOY_GROWTH = 'EPS Diluted (Annual YoY Growth)', 'earnings_per_share_diluted_yoy_growth_fy', 'percent', False, False
    EPS_DILUTED_FY = 'EPS Diluted (FY)', 'last_annual_eps', 'currency', False, False
    EPS_DILUTED_MRQ = 'EPS Diluted (MRQ)', 'earnings_per_share_fq', 'currency', False, False
    EPS_DILUTED_QUARTERLY_QOQ_GROWTH = 'EPS Diluted (Quarterly QoQ Growth)', 'earnings_per_share_diluted_qoq_growth_fq', 'percent', False, False
    EPS_DILUTED_QUARTERLY_YOY_GROWTH = 'EPS Diluted (Quarterly YoY Growth)', 'earnings_per_share_diluted_yoy_growth_fq', 'percent', False, False
    EPS_DILUTED_TTM = 'EPS Diluted (TTM)', 'earnings_per_share_diluted_ttm', 'currency', False, False
    EPS_DILUTED_TTM_YOY_GROWTH = 'EPS Diluted (TTM YoY Growth)', 'earnings_per_share_diluted_yoy_growth_ttm', 'percent', False, False
    EPS_FORECAST_MRQ = 'EPS Forecast (MRQ)', 'earnings_per_share_forecast_next_fq', 'currency', False, False
    EXCHANGE = 'Exchange', 'exchange', 'text', False, False
    EXPONENTIAL_MOVING_AVERAGE_10 = 'Exponential Moving Average (10)', 'EMA10', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_100 = 'Exponential Moving Average (100)', 'EMA100', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_20 = 'Exponential Moving Average (20)', 'EMA20', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_200 = 'Exponential Moving Average (200)', 'EMA200', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_30 = 'Exponential Moving Average (30)', 'EMA30', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_5 = 'Exponential Moving Average (5)', 'EMA5', 'computed_recommendation', True, False
    EXPONENTIAL_MOVING_AVERAGE_50 = 'Exponential Moving Average (50)', 'EMA50', 'computed_recommendation', True, False
    FREE_CASH_FLOW_ANNUAL_YOY_GROWTH = 'Free Cash Flow (Annual YoY Growth)', 'free_cash_flow_yoy_growth_fy', 'percent', False, False
    FREE_CASH_FLOW_MARGIN_FY = 'Free Cash Flow Margin (FY)', 'free_cash_flow_margin_fy', 'percent', False, False
    FREE_CASH_FLOW_MARGIN_TTM = 'Free Cash Flow Margin (TTM)', 'free_cash_flow_margin_ttm', 'percent', False, False
    FREE_CASH_FLOW_QUARTERLY_QOQ_GROWTH = 'Free Cash Flow (Quarterly QoQ Growth)', 'free_cash_flow_qoq_growth_fq', 'percent', False, False
    FREE_CASH_FLOW_QUARTERLY_YOY_GROWTH = 'Free Cash Flow (Quarterly YoY Growth)', 'free_cash_flow_yoy_growth_fq', 'percent', False, False
    FREE_CASH_FLOW_TTM_YOY_GROWTH = 'Free Cash Flow (TTM YoY Growth)', 'free_cash_flow_yoy_growth_ttm', 'percent', False, False
    FUNDAMENTAL_CURRENCY_CODE = 'Fundamental Currency Code', 'fundamental_currency_code', 'text', False, False
    GAP_PERCENT = 'Gap %', 'gap', 'percent', True, False
    GOODWILL = 'Goodwill', 'goodwill', 'currency', False, False
    GROSS_MARGIN_FY = 'Gross Margin (FY)', 'gross_profit_margin_fy', 'percent', False, False
    GROSS_MARGIN_TTM = 'Gross Margin (TTM)', 'gross_margin', 'percent', False, False
    GROSS_PROFIT_ANNUAL_YOY_GROWTH = 'Gross Profit (Annual YoY Growth)', 'gross_profit_yoy_growth_fy', 'percent', False, False
    GROSS_PROFIT_FY = 'Gross Profit (FY)', 'gross_profit', 'currency', False, False
    GROSS_PROFIT_MRQ = 'Gross Profit (MRQ)', 'gross_profit_fq', 'currency', False, False
    GROSS_PROFIT_QUARTERLY_QOQ_GROWTH = 'Gross Profit (Quarterly QoQ Growth)', 'gross_profit_qoq_growth_fq', 'percent', False, False
    GROSS_PROFIT_QUARTERLY_YOY_GROWTH = 'Gross Profit (Quarterly YoY Growth)', 'gross_profit_yoy_growth_fq', 'percent', False, False
    GROSS_PROFIT_TTM_YOY_GROWTH = 'Gross Profit (TTM YoY Growth)', 'gross_profit_yoy_growth_ttm', 'percent', False, False
    HIGH = 'High', 'high', 'currency', True, False
    HULL_MOVING_AVERAGE_9 = 'Hull Moving Average (9)', 'HullMA9', 'recommendation', True, False
    ICHIMOKU_BASE_LINE_9_26_52_26 = 'Ichimoku Base Line (9, 26, 52, 26)', 'Ichimoku.BLine', 'computed_recommendation', True, False
    ICHIMOKU_CONVERSION_LINE_9_26_52_26 = 'Ichimoku Conversion Line (9, 26, 52, 26)', 'Ichimoku.CLine', 'round', True, False
    ICHIMOKU_LEADING_SPAN_A_9_26_52_26 = 'Ichimoku Leading Span A (9, 26, 52, 26)', 'Ichimoku.Lead1', 'float', True, False
    ICHIMOKU_LEADING_SPAN_B_9_26_52_26 = 'Ichimoku Leading Span B (9, 26, 52, 26)', 'Ichimoku.Lead2', 'float', True, False
    INDUSTRY = 'Industry', 'industry', 'text', False, False
    KELTNER_CHANNELS_LOWER_BAND_20 = 'Keltner Channels Lower Band (20)', 'KltChnl.lower', 'float', True, False
    KELTNER_CHANNELS_UPPER_BAND_20 = 'Keltner Channels Upper Band (20)', 'KltChnl.upper', 'float', True, False
    LAST_YEAR_REVENUE_FY = 'Last Year Revenue (FY)', 'last_annual_revenue', 'currency', False, False
    LOGOID = 'Logoid', 'logoid', 'text', False, False
    LOW = 'Low', 'low', 'currency', True, False
    MACD_LEVEL_12_26 = 'MACD Level (12, 26)', 'MACD.macd', 'computed_recommendation', True, False
    MACD_SIGNAL_12_26 = 'MACD Signal (12, 26)', 'MACD.signal', 'float', True, False
    MARKET_CAPITALIZATION = 'Market Capitalization', 'market_cap_basic', 'currency', False, False
    MOMENTUM_10 = 'Momentum (10)', 'Mom', 'computed_recommendation', True, True
    MONEY_FLOW_14 = 'Money Flow (14)', 'MoneyFlow', 'round', True, False
    MONTHLY_PERFORMANCE = 'Monthly Performance', 'Perf.1M', 'percent', False, False
    MONTH_HIGH_1 = '1-Month High', 'High.1M', 'round', False, False
    MONTH_HIGH_3 = '3-Month High', 'High.3M', 'round', False, False
    MONTH_HIGH_6 = '6-Month High', 'High.6M', 'round', False, False
    MONTH_LOW_1 = '1-Month Low', 'Low.1M', 'round', False, False
    MONTH_LOW_3 = '3-Month Low', 'Low.3M', 'round', False, False
    MONTH_LOW_6 = '6-Month Low', 'Low.6M', 'round', False, False
    MONTH_PERFORMANCE_3 = '3-Month Performance', 'Perf.3M', 'percent', False, False
    MONTH_PERFORMANCE_6 = '6-Month Performance', 'Perf.6M', 'percent', False, False
    MOVING_AVERAGES_RATING = 'Moving Averages Rating', 'Recommend.MA', 'rating', True, False
    NAME = 'Name', 'name', 'text', False, False
    NEGATIVE_DIRECTIONAL_INDICATOR_14 = 'Negative Directional Indicator (14)', 'ADX-DI', 'round', True, True
    NET_DEBT_MRQ = 'Net Debt (MRQ)', 'net_debt', 'currency', False, False
    NET_INCOME_ANNUAL_YOY_GROWTH = 'Net Income (Annual YoY Growth)', 'net_income_yoy_growth_fy', 'percent', False, False
    NET_INCOME_FY = 'Net Income (FY)', 'net_income', 'currency', False, False
    NET_INCOME_QUARTERLY_QOQ_GROWTH = 'Net Income (Quarterly QoQ Growth)', 'net_income_qoq_growth_fq', 'percent', False, False
    NET_INCOME_QUARTERLY_YOY_GROWTH = 'Net Income (Quarterly YoY Growth)', 'net_income_yoy_growth_fq', 'percent', False, False
    NET_INCOME_TTM_YOY_GROWTH = 'Net Income (TTM YoY Growth)', 'net_income_yoy_growth_ttm', 'percent', False, False
    NET_MARGIN_FY = 'Net Margin (FY)', 'net_income_bef_disc_oper_margin_fy', 'percent', False, False
    NET_MARGIN_TTM = 'Net Margin (TTM)', 'after_tax_margin', 'percent', False, False
    NUMBER_OF_EMPLOYEES = 'Number of Employees', 'number_of_employees', 'number_group', False, False
    NUMBER_OF_SHAREHOLDERS = 'Number of Shareholders', 'number_of_shareholders', 'number_group', False, False
    OPEN = 'Open', 'open', 'currency', True, False
    OPERATING_MARGIN_FY = 'Operating Margin (FY)', 'oper_income_margin_fy', 'percent', False, False
    OPERATING_MARGIN_TTM = 'Operating Margin (TTM)', 'operating_margin', 'percent', False, False
    OSCILLATORS_RATING = 'Oscillators Rating', 'Recommend.Other', 'rating', True, False
    PARABOLIC_SAR = 'Parabolic SAR', 'P.SAR', 'computed_recommendation', True, False
    PATTERN = 'Pattern', 'candlestick', 'missing', True, False
    PIVOT_CAMARILLA_P = 'Pivot Camarilla P', 'Pivot.M.Camarilla.Middle', 'round', True, False
    PIVOT_CAMARILLA_R1 = 'Pivot Camarilla R1', 'Pivot.M.Camarilla.R1', 'round', True, False
    PIVOT_CAMARILLA_R2 = 'Pivot Camarilla R2', 'Pivot.M.Camarilla.R2', 'round', True, False
    PIVOT_CAMARILLA_R3 = 'Pivot Camarilla R3', 'Pivot.M.Camarilla.R3', 'round', True, False
    PIVOT_CAMARILLA_S1 = 'Pivot Camarilla S1', 'Pivot.M.Camarilla.S1', 'round', True, False
    PIVOT_CAMARILLA_S2 = 'Pivot Camarilla S2', 'Pivot.M.Camarilla.S2', 'round', True, False
    PIVOT_CAMARILLA_S3 = 'Pivot Camarilla S3', 'Pivot.M.Camarilla.S3', 'round', True, False
    PIVOT_CLASSIC_P = 'Pivot Classic P', 'Pivot.M.Classic.Middle', 'round', True, False
    PIVOT_CLASSIC_R1 = 'Pivot Classic R1', 'Pivot.M.Classic.R1', 'round', True, False
    PIVOT_CLASSIC_R2 = 'Pivot Classic R2', 'Pivot.M.Classic.R2', 'round', True, False
    PIVOT_CLASSIC_R3 = 'Pivot Classic R3', 'Pivot.M.Classic.R3', 'round', True, False
    PIVOT_CLASSIC_S1 = 'Pivot Classic S1', 'Pivot.M.Classic.S1', 'round', True, False
    PIVOT_CLASSIC_S2 = 'Pivot Classic S2', 'Pivot.M.Classic.S2', 'round', True, False
    PIVOT_CLASSIC_S3 = 'Pivot Classic S3', 'Pivot.M.Classic.S3', 'round', True, False
    PIVOT_DM_P = 'Pivot DM P', 'Pivot.M.Demark.Middle', 'round', True, False
    PIVOT_DM_R1 = 'Pivot DM R1', 'Pivot.M.Demark.R1', 'round', True, False
    PIVOT_DM_S1 = 'Pivot DM S1', 'Pivot.M.Demark.S1', 'round', True, False
    PIVOT_FIBONACCI_P = 'Pivot Fibonacci P', 'Pivot.M.Fibonacci.Middle', 'round', True, False
    PIVOT_FIBONACCI_R1 = 'Pivot Fibonacci R1', 'Pivot.M.Fibonacci.R1', 'round', True, False
    PIVOT_FIBONACCI_R2 = 'Pivot Fibonacci R2', 'Pivot.M.Fibonacci.R2', 'round', True, False
    PIVOT_FIBONACCI_R3 = 'Pivot Fibonacci R3', 'Pivot.M.Fibonacci.R3', 'round', True, False
    PIVOT_FIBONACCI_S1 = 'Pivot Fibonacci S1', 'Pivot.M.Fibonacci.S1', 'round', True, False
    PIVOT_FIBONACCI_S2 = 'Pivot Fibonacci S2', 'Pivot.M.Fibonacci.S2', 'round', True, False
    PIVOT_FIBONACCI_S3 = 'Pivot Fibonacci S3', 'Pivot.M.Fibonacci.S3', 'round', True, False
    PIVOT_WOODIE_P = 'Pivot Woodie P', 'Pivot.M.Woodie.Middle', 'round', True, False
    PIVOT_WOODIE_R1 = 'Pivot Woodie R1', 'Pivot.M.Woodie.R1', 'round', True, False
    PIVOT_WOODIE_R2 = 'Pivot Woodie R2', 'Pivot.M.Woodie.R2', 'round', True, False
    PIVOT_WOODIE_R3 = 'Pivot Woodie R3', 'Pivot.M.Woodie.R3', 'round', True, False
    PIVOT_WOODIE_S1 = 'Pivot Woodie S1', 'Pivot.M.Woodie.S1', 'round', True, False
    PIVOT_WOODIE_S2 = 'Pivot Woodie S2', 'Pivot.M.Woodie.S2', 'round', True, False
    PIVOT_WOODIE_S3 = 'Pivot Woodie S3', 'Pivot.M.Woodie.S3', 'round', True, False
    POSITIVE_DIRECTIONAL_INDICATOR_14 = 'Positive Directional Indicator (14)', 'ADX+DI', 'round', True, True
    POSTMARKET_CHANGE = 'Post-market Change', 'postmarket_change_abs', 'missing', False, False
    POSTMARKET_CHANGE_PERCENT = 'Post-market Change %', 'postmarket_change', 'missing', False, False
    POSTMARKET_CLOSE = 'Post-market Close', 'postmarket_close', 'missing', False, False
    POSTMARKET_HIGH = 'Post-market High', 'postmarket_high', 'missing', False, False
    POSTMARKET_LOW = 'Post-market Low', 'postmarket_low', 'missing', False, False
    POSTMARKET_OPEN = 'Post-market Open', 'postmarket_open', 'missing', False, False
    POSTMARKET_VOLUME = 'Post-market Volume', 'postmarket_volume', 'missing', False, False
    PREMARKET_CHANGE = 'Pre-market Change', 'premarket_change_abs', 'currency', False, False
    PREMARKET_CHANGE_FROM_OPEN = 'Pre-market Change from Open', 'premarket_change_from_open_abs', 'round', False, False
    PREMARKET_CHANGE_FROM_OPEN_PERCENT = 'Pre-market Change from Open %', 'premarket_change_from_open', 'percent', False, False
    PREMARKET_CHANGE_PERCENT = 'Pre-market Change %', 'premarket_change', 'percent', False, False
    PREMARKET_CLOSE = 'Pre-market Close', 'premarket_close', 'currency', False, False
    PREMARKET_GAP_PERCENT = 'Pre-market Gap %', 'premarket_gap', 'percent', False, False
    PREMARKET_HIGH = 'Pre-market High', 'premarket_high', 'currency', False, False
    PREMARKET_LOW = 'Pre-market Low', 'premarket_low', 'currency', False, False
    PREMARKET_OPEN = 'Pre-market Open', 'premarket_open', 'currency', False, False
    PREMARKET_VOLUME = 'Pre-market Volume', 'premarket_volume', 'number_group', False, False
    PRETAX_MARGIN_TTM = 'Pretax Margin (TTM)', 'pre_tax_margin', 'percent', False, False
    PRICE = 'Price', 'close', 'currency', True, False
    PRICE_TO_BOOK_FY = 'Price to Book (FY)', 'price_book_ratio', 'round', False, False
    PRICE_TO_BOOK_MRQ = 'Price to Book (MRQ)', 'price_book_fq', 'round', False, False
    PRICE_TO_EARNINGS_RATIO_TTM = 'Price to Earnings Ratio (TTM)', 'price_earnings_ttm', 'round', False, False
    PRICE_TO_FREE_CASH_FLOW_TTM = 'Price to Free Cash Flow (TTM)', 'price_free_cash_flow_ttm', 'round', False, False
    PRICE_TO_REVENUE_RATIO_TTM = 'Price to Revenue Ratio (TTM)', 'price_revenue_ttm', 'round', False, False
    PRICE_TO_SALES_FY = 'Price to Sales (FY)', 'price_sales_ratio', 'round', False, False
    QUICK_RATIO_MRQ = 'Quick Ratio (MRQ)', 'quick_ratio', 'round', False, False
    RATE_OF_CHANGE_9 = 'Rate Of Change (9)', 'ROC', 'round', True, False
    RECENT_EARNINGS_DATE = 'Recent Earnings Date', 'earnings_release_date', 'date', False, False
    RELATIVE_STRENGTH_INDEX_14 = 'Relative Strength Index (14)', 'RSI', 'computed_recommendation', True, True
    RELATIVE_STRENGTH_INDEX_7 = 'Relative Strength Index (7)', 'RSI7', 'computed_recommendation', True, True
    RELATIVE_VOLUME = 'Relative Volume', 'relative_volume_10d_calc', 'round', True, False
    RELATIVE_VOLUME_AT_TIME = 'Relative Volume at Time', 'relative_volume_intraday.5', 'round', False, False
    RESEARCH_AND_DEVELOPMENT_RATIO_FY = 'Research & development Ratio (FY)', 'research_and_dev_ratio_fy', 'percent', False, False
    RESEARCH_AND_DEVELOPMENT_RATIO_TTM = 'Research & development Ratio (TTM)', 'research_and_dev_ratio_ttm', 'percent', False, False
    RETURN_ON_ASSETS_TTM = 'Return on Assets (TTM)', 'return_on_assets', 'round', False, False
    RETURN_ON_EQUITY_TTM = 'Return on Equity (TTM)', 'return_on_equity', 'round', False, False
    RETURN_ON_INVESTED_CAPITAL_TTM = 'Return on Invested Capital (TTM)', 'return_on_invested_capital', 'percent', False, False
    REVENUE_ANNUAL_YOY_GROWTH = 'Revenue (Annual YoY Growth)', 'total_revenue_yoy_growth_fy', 'percent', False, False
    REVENUE_PER_EMPLOYEE_FY = 'Revenue per Employee (FY)', 'revenue_per_employee', 'currency', False, False
    REVENUE_QUARTERLY_QOQ_GROWTH = 'Revenue (Quarterly QoQ Growth)', 'total_revenue_qoq_growth_fq', 'percent', False, False
    REVENUE_QUARTERLY_YOY_GROWTH = 'Revenue (Quarterly YoY Growth)', 'total_revenue_yoy_growth_fq', 'percent', False, False
    REVENUE_TTM_YOY_GROWTH = 'Revenue (TTM YoY Growth)', 'total_revenue_yoy_growth_ttm', 'percent', False, False
    SECTOR = 'Sector', 'sector', 'text', False, False
    SELLING_GENERAL_AND_ADMIN_EXPENSES_RATIO_FY = 'Selling General & Admin expenses Ratio (FY)', 'sell_gen_admin_exp_other_ratio_fy', 'percent', False, False
    SELLING_GENERAL_AND_ADMIN_EXPENSES_RATIO_TTM = 'Selling General & Admin expenses Ratio (TTM)', 'sell_gen_admin_exp_other_ratio_ttm', 'percent', False, False
    SHARES_FLOAT = 'Shares Float', 'float_shares_outstanding', 'number_group', False, False
    SIMPLE_MOVING_AVERAGE_10 = 'Simple Moving Average (10)', 'SMA10', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_100 = 'Simple Moving Average (100)', 'SMA100', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_20 = 'Simple Moving Average (20)', 'SMA20', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_200 = 'Simple Moving Average (200)', 'SMA200', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_30 = 'Simple Moving Average (30)', 'SMA30', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_5 = 'Simple Moving Average (5)', 'SMA5', 'computed_recommendation', True, False
    SIMPLE_MOVING_AVERAGE_50 = 'Simple Moving Average (50)', 'SMA50', 'computed_recommendation', True, False
    STOCHASTIC_PERCENTD_14_3_3 = 'Stochastic %D (14, 3, 3)', 'Stoch.D', 'round', True, True
    STOCHASTIC_PERCENTK_14_3_3 = 'Stochastic %K (14, 3, 3)', 'Stoch.K', 'computed_recommendation', True, True
    STOCHASTIC_RSI_FAST_3_3_14_14 = 'Stochastic RSI Fast (3, 3, 14, 14)', 'Stoch.RSI.K', 'computed_recommendation', True, False
    STOCHASTIC_RSI_SLOW_3_3_14_14 = 'Stochastic RSI Slow (3, 3, 14, 14)', 'Stoch.RSI.D', 'round', True, False
    SUBMARKET = 'Submarket', 'submarket', 'missing', False, False
    SUBTYPE = 'Subtype', 'subtype', 'text', False, False
    TECHNICAL_RATING = 'Technical Rating', 'Recommend.All', 'rating', True, False
    TOTAL_ASSETS_ANNUAL_YOY_GROWTH = 'Total Assets (Annual YoY Growth)', 'total_assets_yoy_growth_fy', 'percent', False, False
    TOTAL_ASSETS_MRQ = 'Total Assets (MRQ)', 'total_assets', 'currency', False, False
    TOTAL_ASSETS_QUARTERLY_QOQ_GROWTH = 'Total Assets (Quarterly QoQ Growth)', 'total_assets_qoq_growth_fq', 'percent', False, False
    TOTAL_ASSETS_QUARTERLY_YOY_GROWTH = 'Total Assets (Quarterly YoY Growth)', 'total_assets_yoy_growth_fq', 'percent', False, False
    TOTAL_CURRENT_ASSETS_MRQ = 'Total Current Assets (MRQ)', 'total_current_assets', 'currency', False, False
    TOTAL_DEBT_ANNUAL_YOY_GROWTH = 'Total Debt (Annual YoY Growth)', 'total_debt_yoy_growth_fy', 'percent', False, False
    TOTAL_DEBT_MRQ = 'Total Debt (MRQ)', 'total_debt', 'currency', False, False
    TOTAL_DEBT_QUARTERLY_QOQ_GROWTH = 'Total Debt (Quarterly QoQ Growth)', 'total_debt_qoq_growth_fq', 'percent', False, False
    TOTAL_DEBT_QUARTERLY_YOY_GROWTH = 'Total Debt (Quarterly YoY Growth)', 'total_debt_yoy_growth_fq', 'percent', False, False
    TOTAL_LIABILITIES_FY = 'Total Liabilities (FY)', 'total_liabilities_fy', 'currency', False, False
    TOTAL_LIABILITIES_MRQ = 'Total Liabilities (MRQ)', 'total_liabilities_fq', 'currency', False, False
    TOTAL_REVENUE_FY = 'Total Revenue (FY)', 'total_revenue', 'currency', False, False
    TOTAL_SHARES_OUTSTANDING = 'Total Shares Outstanding', 'total_shares_outstanding_fundamental', 'number_group', False, False
    TYPE = 'Type', 'type', 'text', False, False
    ULTIMATE_OSCILLATOR_7_14_28 = 'Ultimate Oscillator (7, 14, 28)', 'UO', 'recommendation', True, False
    UPCOMING_EARNINGS_DATE = 'Upcoming Earnings Date', 'earnings_release_next_date', 'date', False, False
    VOLATILITY = 'Volatility', 'Volatility.D', 'percent', False, False
    VOLATILITY_MONTH = 'Volatility Month', 'Volatility.M', 'percent', False, False
    VOLATILITY_WEEK = 'Volatility Week', 'Volatility.W', 'percent', False, False
    VOLUME = 'Volume', 'volume', 'number_group', True, False
    VOLUMEXPRICE = 'Volume*Price', 'Value.Traded', 'number_group', True, False
    VOLUME_WEIGHTED_AVERAGE_PRICE = 'Volume Weighted Average Price', 'VWAP', 'float', True, False
    VOLUME_WEIGHTED_MOVING_AVERAGE_20 = 'Volume Weighted Moving Average (20)', 'VWMA', 'recommendation', True, False
    WEEKLY_PERFORMANCE = 'Weekly Performance', 'Perf.W', 'percent', False, False
    WEEK_HIGH_52 = '52 Week High', 'price_52_week_high', 'round', False, False
    WEEK_LOW_52 = '52 Week Low', 'price_52_week_low', 'round', False, False
    WILLIAMS_PERCENT_RANGE_14 = 'Williams Percent Range (14)', 'W.R', 'computed_recommendation', True, False
    YEARLY_PERFORMANCE = 'Yearly Performance', 'Perf.Y', 'percent', False, False
    YEAR_BETA_1 = '1-Year Beta', 'beta_1_year', 'round', False, False
    YTD_PERFORMANCE = 'YTD Performance', 'Perf.YTD', 'percent', False, False
    Y_PERFORMANCE_5 = '5Y Performance', 'Perf.5Y', 'percent', False, False