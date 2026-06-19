def check_data_quality(df, threshold=0.1):
    '''
    Analyzes columns for missing data and raises an error if the threshold is exceeded.
    
    Args:
        df: DataFrame to analyze.
        threshold: Maximum tolerated percentage of nulls (e.g., 0.1 for 1%).
    
    Raises:
        ValueError: If any column has more nulls than allowed.
    '''
    print(f"🔍 STARTING QUALITY CHECK (Threshold: {threshold:.0%})")
    print("-" * 65)
    print(f"{'COLUMN':<25} | {'NULLS':<10} | {'%':<10} | STATUS")
    print("-" * 65)
    
    bad_columns = []
    
    for col in df.columns:
        # Calculate nulls
        missing_count = df[col].isnull().sum()
        missing_pct = missing_count / len(df)
        
        # Define visual status
        if missing_pct > threshold:
            status = "❌ FAILED"
            bad_columns.append(f"{col} ({missing_pct:.1%})")
        elif missing_pct > 0:
            status = "⚠️ WARNING"
        else:
            status = "✅ OK"
            
        print(f"{col:<25} | {missing_count:<10} | {missing_pct:<10.1%} | {status}")

    print("-" * 65)
    
    # If there are bad columns, stop everything!
    if bad_columns:
        error_msg = f"Critical Quality Issue! The following columns exceeded {threshold:.0%} nulls: {', '.join(bad_columns)}"
        raise ValueError(error_msg)
        
    print("🎉 All data is within quality parameters!")