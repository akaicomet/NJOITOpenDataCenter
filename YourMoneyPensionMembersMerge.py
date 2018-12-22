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

    _data1.loc[_data1._20_year_status == 'YES', '_20_year_status'] = '1'  
    _data1.loc[_data1._20_year_status == 'NO', '_20_year_status'] = '0'  

    _data1.loc[_data1.veteran_status == 'YES', 'veteran_status'] = '1'  
    _data1.loc[_data1.veteran_status == 'NO', 'veteran_status'] = '0'
	
    _data1['_20_year_status'] = _data1['_20_year_status'].astype(int)	
    _data1['veteran_status'] = _data1['veteran_status'].astype(int)
    _data1['all_employers_salary_amt'] = _data1['all_employers_salary_amt'].astype(float)	
    _data1['current_employer_salary_amt'] = _data1['current_employer_salary_amt'].astype(float)	
    _data1['employer_name'] = _data1['employer_name'].astype(str)	
    _data1['location_code'] = _data1['location_code'].astype(int)
    _data1['location_name'] = _data1['location_name'].astype(str)	
    _data1['member_first_name'] = _data1['member_first_name'].astype(str)
    _data1['member_last_name'] = _data1['member_last_name'].astype(str)
    _data1['member_mi'] = _data1['member_mi'].astype(str)
    _data1['membership_tier'] = _data1['membership_tier'].astype(int)
    _data1['pension_fund_id'] = _data1['pension_fund_id'].astype(int)
    _data1['pension_fund_name'] = _data1['pension_fund_name'].astype(str)	
    #_data1['pension_group_id'] = _data1['pension_group_id'].astype(int)
    _data1['service_months_qty'] = _data1['service_months_qty'].astype(int)
    _data1['service_years_qty'] = _data1['service_years_qty'].astype(int)	
    _data1['total_months_qty'] = _data1['total_months_qty'].astype(int)	
    _data1['veteran_status'] = _data1['veteran_status'].astype(str)	
    _data1['member_middle_initial'] = _data1['member_middle_initial'].astype(str)

    #pension paid members statistic	
    _data1['pension_fund_name_enc'] = _data1.groupby('pension_fund_name')['IsPensionPaid'].transform('mean')
    _data1['pension_group_name_enc'] = _data1.groupby('pension_group_id')['IsPensionPaid'].transform('mean')

    _data1 = _data1.fillna(0)
    
    return _data1	
