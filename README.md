# NJOITOpenDataCenter Pension Record Data
Governor Christie’s 2010 YourMoney web site was a groundbreaking (and award‐winning) enabler of government transparency. It delivered to the public, for the first time, formal and consistent access to the State’s financial‐ related data. The Open Data Center (ODC) extends this capability to all State data – not just financial data. Data is also better organized and described.

## YourMoney Active Pension Members
The data file reflects data for employees who are active members in a state pension system as reported by the employer. It lists the salary eligible for pension credit for the four most recent calendar quarters reported as well as attributes that describe the status of the member for pension purposes. Additional information is in the attached dataset summary PDF (available on the [About] tab under "Attachments").

## YourMoney Retired Pension Members
This dataset contains pension benefit data for retired employees paid through a State retirement system. The data reflects year-to-date payments and the monthly allowances for each pensioner during the time period noted. Additional information is in the attached dataset summary PDF (available on the [About] tab under "Attachments".).

## Main Components of code

### ETL and Data Cleansing  
YourMoneyActivePensionMembers.py	
YourMoneyPensionMembersMerge.py	
YourMoneyRetiredPensionMembers.py

### Feture Engineering 1
feature_importance_RFECV2 in AutoFeatureEngineering.py [[Wiki]](https://github.com/akaicomet/Portuguese-Bank-Marketing/wiki/Recursive-Feature-Elimination-and-Cross-validated-selection-(RFEC)-with-sets-of-learning-classifier-and-data-transformation)

### Feture Engineering 2
XRayChart in X-Ray_Scan.py [[Wiki]](https://github.com/akaicomet/Portuguese-Bank-Marketing/wiki/Data-Transformation-and-Feature-Extraction)

### ML Classifier Algorithm Selection
MLModelBuilding in ML_Auto.py [[Wiki]]( https://github.com/akaicomet/Portuguese-Bank-Marketing/wiki/Machine-Learning-Model-Building-in-ML_Auto-Module)
