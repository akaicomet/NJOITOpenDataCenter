def PensionMembersMerge(_data1,_data2):
    _data1 = pd.merge(
        left=_data1, 
        right=_data2[['member_frst_name', 'member_last_name','member_birth_year','member_middle_initial', 'member_last_employer']].drop_duplicates(),  
		left_on=['member_first_name', 'member_last_name','member_mi','employer_name'], 
        right_on=['member_frst_name', 'member_last_name','member_middle_initial', 'member_last_employer'],    
        how='left'
    )
    _data1.loc[_data1.member_last_employer.isnull()==False, 'IsPensionPaid'] = 1

    _data1 = pd.merge( 
        left=_data1[['_20_year_status',  'all_employers_salary_amt',  'current_employer_salary_amt', 'employer_name', 'enrollment_date', 'location_code', 'location_name', 'member_first_name', 'member_last_name', 'member_mi', 'membership_tier', 'pension_fund_id', 'pension_fund_name', 'pension_group_id',  'service_months_qty', 'service_years_qty', 'total_months_qty', 'veteran_status', 'current_employer_salary_rollingamt', 'employer_rollingcnt', 'IsPensionPaid']], 
        right=_data2[['member_frst_name', 'member_last_name','member_birth_year', 'member_last_employer']].drop_duplicates(),  
        left_on=['member_first_name', 'member_last_name','employer_name'], 
        right_on=['member_frst_name', 'member_last_name','member_last_employer'],    
        how='left'
    )
    _data1.loc[(_data1.member_last_employer.isnull()==False) & (_data1.IsPensionPaid != 1), 'IsPensionPaid'] = 1

    _data1 = pd.merge(
        left=_data1[['_20_year_status', 'all_employers_salary_amt',  'current_employer_salary_amt', 'employer_name', 'enrollment_date', 'location_code', 'location_name', 'member_first_name', 'member_last_name', 'member_mi', 'membership_tier', 'pension_fund_id', 'pension_fund_name', 'pension_group_id',  'service_months_qty', 'service_years_qty', 'total_months_qty', 'veteran_status', 'current_employer_salary_rollingamt', 'employer_rollingcnt', 'IsPensionPaid']],   
        right=_data2[['member_frst_name', 'member_middle_initial', 'member_last_name','member_birth_year']].drop_duplicates(),  
        left_on=['member_first_name', 'member_mi', 'member_last_name'], 
        right_on=['member_frst_name', 'member_middle_initial', 'member_last_name'],    
        how='left'
    )
    _data1.loc[(_data1.member_birth_year.isnull()==False) & (_data1.IsPensionPaid != 1), 'IsPensionPaid'] = 1
    _data1.loc[(_data1.member_birth_year.isnull()==True) & (_data1.IsPensionPaid != 1), 'IsPensionPaid'] = 0
    _data1 = _data1.drop(columns=['member_frst_name', 'member_birth_year']).loc[(_data1._20_year_status == 'YES')  | (_data1.IsPensionPaid == 1)] 

    _freq_pensioned = _data1[_data1.IsPensionPaid == 1].groupby(['employer_name','IsPensionPaid'], as_index=False)['IsPensionPaid'].agg([ 'count']).reset_index()[['employer_name','count']].rename(columns={'count': 'employer_freq_pensioned'})

    _data1 = pd.merge(
        left=_data1, 
        right=_freq_pensioned,  
        left_on=['employer_name'], 
        right_on=['employer_name'],
        how='left'
    )

    _freq_pensioned = _data1[_data1.IsPensionPaid == 1].groupby(['location_name','IsPensionPaid'], as_index=False)['IsPensionPaid'].agg([ 'count']).reset_index()[['location_name','count']].rename(columns={'count': 'location_freq_pensioned'})

    _data1 = pd.merge(
        left=_data1, 
        right=_freq_pensioned,  
        left_on=['location_name'], 
        right_on=['location_name'],
        how='left'
    )

    _freq_pensioned = _data1[_data1.IsPensionPaid == 1].groupby(['pension_fund_name','IsPensionPaid'], as_index=False)['IsPensionPaid'].agg([ 'count']).reset_index()[['pension_fund_name','count']].rename(columns={'count': 'pension_freq_pensioned'})

    _data1 = pd.merge(
        left=_data1, 
        right=_freq_pensioned,  
        left_on=['pension_fund_name'], 
        right_on=['pension_fund_name'],
        how='left'
    )

    _data1.loc[_data1._20_year_status == 'YES', '_20_year_status'] = 1  
    _data1.loc[_data1._20_year_status == 'NO', '_20_year_status'] = 0  

    _data1.loc[_data1.veteran_status == 'YES', 'veteran_status'] = 1  
    _data1.loc[_data1.veteran_status == 'NO', 'veteran_status'] = 0 
