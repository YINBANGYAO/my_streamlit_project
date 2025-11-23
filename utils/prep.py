import pandas as pd

def preprocess_data(df):
    """
    Transform: Fix temporal ordering for correct time-series visualization.
    """
    # Ensure we work on a copy
    df = df.copy()
    
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    # Convert to Categorical to ensure chronological sorting in charts
    df['release_month'] = pd.Categorical(df['release_month'], categories=month_order, ordered=True)
    
    return df