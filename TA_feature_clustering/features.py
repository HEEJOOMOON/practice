import pandas as pd
import pandas_ta as ta


def momentum(series: pd.DataFrame,
             fast: int=12,
             slow: int=26,
             period: int=14):

    df = pd.DataFrame()
    df['ao'] = ta.ao(series.high, series.open, fast=fast, slow=slow)
    df['cci'] = ta.cci(series.high, series.low, series.close, length=period)
    df['mom'] = ta.mom(series.close, length=period)
    df['ppo'] = ta.ppo(series.close, fast=fast, slow=slow)
    df['rsi'] = ta.rsi(series.close, length=period)
    df['tsi'] = ta.tsi(series.close, fast=fast, slow=slow)
    df['willr'] = ta.willr(series.high, series.low, series.close, length=period)
    df['macd'] = ta.macd(series.close, fast=fast, slow=slow)
    df['apo'] = ta.apo(series.close, fast=fast, slow=slow)

    return df


def trend(series: pd.DataFrame,
          period: int=14):

    df = pd.DataFrame()
    df['adx'] = ta.adx(series.high, series.low, series.close, length=period)
    df['aroon'] = ta.aroon(series.high, series.low, length=period)
    df['dpo'] = ta.dpo(series.close, length=period)

    return df


def volume(series: pd.DataFrame):

    df = pd.DataFrame()
    df['ad'] = ta.ad(series.high, series.low, series.close, series.volume)
    df['obv'] = ta.obv(series.close, series.volume)

    return df

def volatility(series: pd.DataFrame,
               period: int=14):

    df = pd.DataFrame()
    df['atr'] = ta.atr(series.high, series.low, series.close, length=period)
    df['trange'] = ta.true_range(series.high, series.low, series.close)

    return df

def price_overlap(series: pd.DataFrame):

    df = pd.DataFrame()
    df['sma_20'] = df.close.rolling(20).mean()
    df['wma_20'] = ta.wma(df.close, length=20)
    df['ema_20'] = ta.ema(df.close, length=20)
    df['sma_60'] = df.close.rolling(60).mean()
    df['wma_60'] = ta.wma(df.close, length=60)
    df['ema_60'] = ta.ema(df.close, length=60)
    df['sma_120'] = df.close.rolling(120).mean()
    df['wma_120'] = ta.wma(df.close, length=120)
    df['ema_120'] = ta.ema(df.close, length=120)
    df['roc_20'] = ta.roc(df.close, length=20)
    df['roc_60'] = ta.roc(df.close, length=60)
    df['roc_120'] = ta.roc(df.close, length=120)
    return df


def features(series: pd.DataFrame,
             fast: int=12,
             slow: int=26,
             period: int=14,):

    momentum_df = momentum(series, fast, slow, period)
    trend_df = trend(series, period)
    volume_df = volume(series)
    volatility_df = volatility(series, period)
    overlap_df = price_overlap(series)

    features_ = pd.concat([momentum_df, trend_df, volatility_df, volume_df, overlap_df],\
                         join='outer', axis=1).reindex(trend_df.index).dropna()

    return features_