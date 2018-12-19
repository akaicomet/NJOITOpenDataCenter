def RetiredPensionMembersDataWrangler(_data):
    RetiredPension_df = pd.DataFrame.from_records(_data)
    #replace 'NA'
    RetiredPension_df['member_middle_initial'].fillna('')

    RetiredPension_df_grped = RetiredPension_df[['report_year_month','member_frst_name','member_middle_initial','member_last_name','member_birth_year','member_last_employer','member_pension_fund','member_retirement_date','ytd_total_paymnts','member_salary_for_calculation']]
    RetiredPension_df_grped= RetiredPension_df_grped.sort_values(['member_last_name','member_frst_name','member_middle_initial','member_birth_year','member_retirement_date','report_year_month']) 
    RetiredPension_df_grped['ytd_total_paymnts'] = RetiredPension_df_grped['ytd_total_paymnts'].astype('float64')
    
    return RetiredPension_df_grped
