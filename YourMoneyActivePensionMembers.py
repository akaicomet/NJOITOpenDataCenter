@exception
def ActivePensionDataWrangler(_data):
    ActivePension_df = pd.DataFrame.from_records(_data)
    #remove duplicate
    ActivePension_df = ActivePension_df.drop_duplicates(ActivePension_df)
    #replace 'NA'
    ActivePension_df['member_mi'].fillna('')
    #remove duplicate
    ActivePension_df = ActivePension_df.drop_duplicates(['_20_year_status','employer_name','enrollment_date','location_code','location_name','member_first_name','member_last_name','member_mi','membership_tier','pension_fund_id','pension_fund_name','pension_group_id','pension_group_name','service_months_qty','service_years_qty','total_months_qty','veteran_status'],keep='last')
    ActivePension_df= ActivePension_df.sort_values(['member_first_name','member_mi','member_last_name','enrollment_date']) 
    #sort value for rolling amount
    ActivePension_df_grped = ActivePension_df[['member_first_name','member_mi','member_last_name','enrollment_date','employer_name','pension_fund_id','current_employer_salary_amt']]
    #replace NA 
    ActivePension_df_grped = ActivePension_df_grped.fillna('-')
    #Aggregation
    ActivePension_df_grped['current_employer_salary_amt'] = ActivePension_df_grped['current_employer_salary_amt'].astype('float64')
    #salary total 
    ActivePension_df_grped['current_employer_salary_rollingamt'] = ActivePension_df_grped.fillna('-').groupby(['member_first_name','member_mi','member_last_name'])['current_employer_salary_amt'].cumsum()
    #count of employers 
    ActivePension_df_grped['employer_rollingcnt'] = ActivePension_df_grped.fillna('-').groupby(['member_first_name','member_mi','member_last_name']).cumcount('enrollment_date')+ 1
    #replace Veteran value
    ActivePension_df.loc[(ActivePension_df.veteran_status == 'NON-VETERAN'), 'veteran_status'] = 'NO'
    ActivePension_df.loc[(ActivePension_df.veteran_status == 'VETERAN'), 'veteran_status'] = 'YES'
    #Populate new variables 
    ActivePension_df2 = pd.merge(
        left=ActivePension_df, 
        right=ActivePension_df_grped[['member_first_name','member_mi','member_last_name','current_employer_salary_rollingamt', 'employer_rollingcnt','enrollment_date','employer_name','pension_fund_id']], 
        left_on=['member_first_name', 'member_last_name', 'member_mi','enrollment_date','employer_name','pension_fund_id'], 
        right_on=['member_first_name', 'member_last_name','member_mi','enrollment_date','employer_name','pension_fund_id'],    
        how='left'
    )
    
    ActivePension_df2['IsPensionPaid'] = np.nan
    
    return ActivePension_df2
