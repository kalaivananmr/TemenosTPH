# Introduction to System Tables - Introductiontosystemtables

> Source: https://docs.temenos.com/docs/Solutions/T24_Transact/Framework/ST/System_Tables/Misc/Introduction.htm#IntroductiontoSystemTables

---

# Introduction to System Tables

Updated On 06 October 2023 |  22 Min(s) read

Feedback
Summarize

The System Tables user guide explains the Customer and related reference tables and the Core Reference tables.

- Customer and related reference tables – This includes the following:
  - The customer application and associated static tables.
  - The customer centric functionalities.
- Core Reference tables – This includes core tables that act as reference for transaction processing as listed below:
  - Country and related tables (like `REGION`, `HOLIDAY` and `DATES`)
  - Currency
  - Category
  - Interest related tables (like Accrual Parameter, Interest Basis, Basic Interest and Periodic Interest)
  - Charge related tables
  - Tax related tables
  - Card Management tables
  - Cheque Management tables
  - Treasury and Settlements related tables
  - Other Core Reference Tables

# Product Configuration

The following system-wide applications help in grouping the customers and defining rules for the group based on the business purposes, like defining customer group specific charges and tax.

- `CONDITION.PRIORITY`
- XXX.GEN.CONDITION and XXX.GROUP.CONDITION, where XXX refers to the business application.
- `APPL.GEN.CONDITION`

## Condition Priority

The purpose of the `CONDITION.PRIORITY` application is to specify, for certain applications, which data elements in other reference applications can be specified to determine condition groups. `CONDITION.PRIORITY` records can be created with the following IDs:

- ACCOUNT
- FIDUCIARY
- FUNDS.TRANSFER
- FX.MARGIN
- LETTER.OF.CREDIT
- SC.MANAGEMENT
- SC.SAFEKEEPING
- SC.TRADING
- STATEMENT
- TAX
- POR.TRANSACTION

`CONDITION.PRIORITY` is a CUS level application. Records of this application can be shared between companies, which share the same customer company, or there could be company-specific `CONDITION.PRIORITY` records by suffixing a hyphen and a Company Code in the ID.

For the `ACCOUNT` application, it is possible to have a specific record for the Company DE0010001 with the ID ACCOUNT-DE0010001.

The (parameters) records without a Company ID suffixed is applicable to the Master Customer Company (specified as *Customer Company* in the `COMPANY` application) as well as to Companies that do not have their own `CONDITION.PRIORITY` records.

An existing `CONDITION.PRIORITY` record cannot be modified. However, it is possible to specify parameters that are applicable in future (after the COB processing on a specified date, which can be either the processing date or any future date) by creating `CONDITION.PRIORITY` records by suffixing a hyphen and a date after the company code in the ID.

The record with ID ’ACCOUNT--20040702’ (with a null Company ID for the customer company) is applicable to the Master Customer Company and the record with ID ‘ACCOUNT-DE0010001-20040702’ is applicable to the Company DE0010001, both records to be effective after the COB processing on 2nd July 2004. The date specified can either be the processing date or it could be a future date.

It is possible to specify the priority items (fields) using the Priority Item field. This is a multi-valued field which defines the order in which fields are used, when matching conditions against values specified in the XXX.GEN.CONDITION records.

- Fields from `CUSTOMER` application can be specified in all `CONDITION.PRIORITY` records.
- Fields from `ACCOUNT` application can be specified only in the `CONDITION.PRIORITY` records related to ACCOUNT or STATEMENT.
- Fields from `SEC.ACC.MASTER` can be specified only in the three `CONDITION.PRIORITY` records related to Wealth application (with IDs SC.MANAGEMENT, SC.SAFEKEEPING and SC.TRADING).

The priority items specified in the `CONDITION.PRIORITY` records are defaulted as the field names in the corresponding XXX.GEN.CONDITION records.

While determining the condition groups of applications, the priority of the data items (specified as *Priority Item*) is determined by their relative position in the `CONDITION.PRIORITY` record.

For each priority item specified in `CONDITION.PRIORITY`, users can also specify a validation, which ensures that a value entered for a priority item (in XXX.GEN.CONDITION applications) exists as a record ID in another table. This can also be used to display an enrichment when the value is entered.



In the `CONDITION.PRIORITY` record for `ACCOUNT`, the *Priority Item* ‘ACCOUNT>CATEGORY’ can have a validation specified in the *Prty Validation* field as ‘CATEGORY>DESCRIPTION’. In this case, when a value for the CATEGORY is entered in `ACCT.GEN.CONDITION`, the value entered should be a valid record ID in the `CATEGORY` application, and the value of the *Description* field in that `CATEGORY` record will be displayed as an enrichment.

## Parameters and Rules for Groups

The XXX.GEN.CONDITION applications provide the parameters to calculate the default groups for some applications. The priority data items, which are used in the XXX.GEN.CONDITION tables, are defaulted from the corresponding `CONDITION.PRIORITY` records.

The XXX.GEN.CONDITION applications and the corresponding `CONDITION.PRIORITY` records from which the priority data items are defaulted are listed below:

| XXX.GEN.CONDITION Applications | CONDITION.PRIORITY record ID from which priority data items are defaulted |
| --- | --- |
| `ACCT.GEN.CONDITION` | ACCOUNT |
| `FD.GEN.CONDITION` | FIDUCIARY |
| `FT.GEN.CONDITION` | FUNDS.TRANSFER |
| `LC.GEN.CONDITION` | LETTER.OF.CREDIT |
| `SCPM.GEN.CONDITION` | SC.MANAGEMENT |
| `SCSK.GEN.CONDITION` | SC.SAFEKEEPING |
| `SCTR.GEN.CONDITION` | SC.TRADING |
| `STMT.GEN.CONDITION` | STATEMENT |
| `TAX.GEN.CONDITION` | TAX |
| `FX.GEN.CONDITION` | FX.MARGIN |
| `PP.GEN.CONDITION` | POR.TRANSACTION |

The parameters specified in `FD.GEN.CONDITION`, `FT.GEN.CONDITION`, `LC.GEN.CONDITION`, `SCPM.GEN.CONDITION`, `SCSK.GEN.CONDITION`, `SCTR.GEN.CONDITION`, `TAX.GEN.CONDITION`, and `PP.GEN.CONDITION` are used to default the condition groups in the `CUSTOMER.CHARGE` application.

The parameters specified in `ACCT.GEN.CONDITION` are used to default the account group (*Condition Group*) in `ACCOUNT`, while those specified in `STMT.GEN.CONDITION` are used to default the frequency in `ACCOUNT.STATEMENT`.

For each XXX.GEN.CONDITION application, there is a corresponding XXX.GROUP.CONDITION application (except for `STMT.GEN.CONDITION`) to define the various parameters for each group. The following XXX.GROUP.CONDITION applications exist:

- `ACCT.GROUP.CONDITION`
- `FD.GROUP.CONDITION`
- `FT.GROUP.CONDITION`
- `LC.GROUP.CONDITION`
- `SCPM.GROUP.CONDITION`
- `SCSK.GROUP.CONDITION`
- `SCTR.GROUP.CONDITION`
- `TAX.TYPE.CONDITION`
- `FX.GROUP.CONDITION`

All the XXX.GEN.CONDITION and XXX.GROUP.CONDITION applications referred here are of the FTD level, which may be company specific or shared between companies depending on the configuration of *Default Finan Com* or *Spcl Fin File* fields in the `COMPANY` record.

If the FTD type files for the Company DE0010001 are unique, then the `ACCT.GEN.CONDITION` records for the Company DE0010001 can have the data items defaulted from the `CONDITION.PRIORITY` record with ID as ‘ACCOUNT-DE0010001’ if that record exists, else from the default `CONDITION.PRIORITY` record with ID as ‘ACCOUNT’.

While defining `CONDITION.PRIORITY` records to be applicable in future, it is possible to specify which XXX.GEN.CONDITION and XXX.GROUP.CONDITION records need to be retained, by specifying their IDs in the *Gen Cond Keep* and *Group Cond Keep* fields respectively. During COB processing on the specified date, these XXX.GEN.CONDITION records are automatically modified with priority data items applicable for the new structure, by retaining existing priority data items and their values. New priority data items are updated with null values.

Further, in conjunction with dated `CONDITION.PRIORITY` records, it is also possible to specify dated XXX.GEN.CONDITION records, which can become effective in future. Such XXX.GEN.CONDITION records are defined by suffixing a hyphen with a date (either processing date or a future date) in the ID. Priority data items in these records are defaulted from the corresponding dated `CONDITION.PRIORITY` records. These record IDs must not be defined as retention record IDs in the *Gen Cond Keep* field of `CONDITION.PRIORITY`.

After COB processing on the specified date, the dated XXX.GEN.CONDITION records replace the corresponding records without a date in the ID.

Those XXX.GEN.CONDITION records that are not included in the *Gen Cond Keep* field of the corresponding dated `CONDITION.PRIORITY` record or those records that do not have a corresponding dated XXX.GEN.CONDITION record are dropped after the COB processing on the specified date.

With the exceptions described below, future dated XXX.GROUP.CONDITION can be created with an ID of the format ‘xxx-Date’, provided the ID is not already specified in the *Group Cond Keep* field of the corresponding dated `CONDITION.PRIORITY` record. After COB processing on the specified date, the dated XXX.GROUP.CONDITION records replace the corresponding records without a date in the ID.

There is an exception to the above referred functionality (which existed before the `CONDITION.PRIORITY` application has been enhanced to accept dated records). The ID format of the `SCPM.GROUP.CONDITION` and `SCSK.GROUP.CONDITION` applications is ‘xxx.date’ (both parts mandatory and connected by a dot) to allow definition of parameters, which applies on various dates. The first part of the ID is validated against the first part of the corresponding XXX.GEN.CONDITION records. When the records in these applications are entered, there is no validation against the `CONDITION.PRIORITY` records.

The XXX.GROUP.CONDITION records whose IDs are not included in the *Group Cond Keep* field of the corresponding dated `CONDITION.PRIORITY` record, or which do not have a corresponding dated XXX.GROUP.CONDITION record (suffixed to the ID with a hyphen and date), will be dropped after the COB processing on the specified date. However, customer-specific XXX.GROUP.CONDITION records with ID format as ‘C-Customer ID’ is not dropped after COB processing.

For Payments, the parameters and conditions applicable for a group of customers is defined in `PP.CLIENT.CONDITIONRECORD` application. Please read [Introduction to Client Conditions](../../../../../Payments/Payments/PP/Payments_Hub_(PP)/Client_Condition/Introduction.htm) for more details.

## Parameter to Default Groups Using Temenos Transact Routine

The `APPL.GEN.CONDITION` application is used to define group conditions for contracts based on a combination of decisions and calls to locally developed subroutines. For example, it allows specific tax codes to be applied to particular types of contract for particular types of customer.

There is one record per application for which many sets of group conditions can be defined. User must ensure that multiple set of groups are defined correctly, as the first set of conditions that pass the validation checks result in that contract group code being applied.



A Temenos Transact subroutine, APPL.GRP.CONDITION can be called to evaluate the current contract record using relevant `APPL.GEN.CONDITON`. It returns the first group code where all decision checks evaluate to true.

The `MM.MONEY.MARKET` and `LD.LOANS.AND.DEPOSIT` applications call the evaluation routine automatically. Other applications can call the evaluation routine from VERSION routines to update local reference fields with the relevant group code.

The subroutine processes these decisions and updates the *Contract Group* field in the application record whenever the contract is changed. If changes to the contract cause the conditions to break, then a new *Contract Group* code is generated, which results in a different tax code being applied. A default group code can be defined as the last group code without associated conditions, if required. `TAX.TYPE.CONDITION` allows the *Contract Group* code to be linked to the allocation of specific tax codes.

## Illustrating Model Parameters

Specifications for System Tables are grouped into different functionalities.

Core Reference tables available in the model bank are given below:

| S.No. | Parameter | Description |
| --- | --- | --- |
| 1. | `COMPANY` | Contains details such as company's name, mnemonic, classification details, applications that are to be run, company level defaults and parameters. |
| 2. | `DATES` | Each company has a Date record, which contains the run dates for the previous, current and the next working day. Batch (overnight) processing system updates the record automatically. |
| 3. | `CONDITION.PRIORITY` | Used to specify the data elements to determine the condition groups for each application. In addition, the order of general conditions to be applied when more than one general condition is involved can also be defined. |
| 4. | `COUNTRY.GROUP` | Used to group the countries based on residence or non-residence when applying charges. |
| 5. | `COUNTRY` | Contains the static details of each country such as country name, currency code and so on. The key for this application must be a standard I.S.O country code. The `CURRENCY` codes must be in the system before setting up the country parameter. |
| 6. | `EB.TIME.ZONES` | Defines the standard zones that have uniform mandated standard time. The ID must be a valid time zone name as specified in the Internet Assigned Numbers Authority (IANA) time zone database. |
| 7. | `HOLIDAY` | - Indicates the public holidays for each country, or region within a country for the calendar year. |
| 8. | `LANGUAGE` | Identifies the languages that are to be used in the system when defining multi-language fields. The Abbreviation code assigned to each Language is used as a screen prompt. |
| 9. | `INTEREST.BASIS` | Determines the component for interest calculation based on the inputs provided in the *INT.BASIS* field. |
| 10. | `CURRENCY.PARAM` | Contains the common details such as *Numeric Currency Code*, *Currency Name*, *Number of Decimal Places* and the *Interest Basis* for each currency. This table ensures that the same numeric code and no of decimals are used on all the different currency files. |
| 11. | `CURRENCY.MARKET` | Helps to identify the correct exchange and revaluation rates to be applied for each currency. |
| 12. | `TRANSACTION` | Contains information about all the Transaction Codes that can be used in Temenos Transact. |
| 13. | `SECTOR` | Sector codes are defined in this table and assigned to each Customer record to group them into broad classifications like Private Sector, Public Sector, and Corporate Banks and so on. |
| 14. | `INDUSTRY` | Helps to define and assign the Industry codes to each Customer record to identify the industry of the customer. |
| 15. | `CATEGORY` | Category codes are used to classify financial transactions in Temenos Transact according to the type of business operation or product. |
| 16. | `AC.CONSOLIDATE.COND` | Allows the user to define the rules for the consolidation of entries for either an Account or a Category record. |
| 17. | `INTERCO.PARAMETER` | Determines if automatic balancing entries are raised when processing transactions in a multi-company or a multi-department (in the same company) environment. |
| 18. | `EB.DUPLICATE.TYPE` | Defines duplicate check criteria for applications. |
| 19. | `EB.LOOKUP` | This is a generic template to hold all the lookups for data access service. The user can create an `EB.LOOKUP` record with the definition and use them as drop-down list in applications. |
| 20. | `EB.SYSTEM.ID` | Provides a description for the *SYSTEM.ID* field in the accounting entry files, which include `STMT.ENTRY`, `CATEG.ENTRY`, `CONSOL.NET.TODAY` and `RE.CONSOL.SPEC.ENTRY`. |
| 21. | `CONSOLIDATE.COND` | The consolidation records hold the consolidation key, series of balance, total debit and credit movement fields. The details are held in for: • Asset and Liability • Profit and Loss |
| 22. | `GROUP.ACCRUAL.PARAM` | This is a parameter file, which holds the options for the bulk accrual of accounts. It reduces the number of accrual accounting entries by consolidating at various levels. |
| 23. | `EB.LOCAL.CONTENT.TABLE` | Stores local context-data on customer records at BNK level. |
| 24. | `ST.ORGANIZATION.STRUCTURE` | Holds the organizational hierarchy of the bank. |
| 25. | `ST.ORGANIZATION.CODE` | Helps to create Organization Codes at each level defined in the `ST.ORGANIZATION.STRUCTURE` application. |
| 26. | `ST.BRANCH` | Holds the branch record, which is updated on authorising the `ST.ORGANIZATION.CODE` record defined for each branch. |
| 27. | `ST.LINE.OF.BUSINESS` | Line of Business is defined to create different Cost Centers for the bank and align them later to a particular branch depending on its requirement. |
| 28. | `CUSTOMER.EXIT.STATUS` | Allows the bank to define the exit statuses and the exit reasons for each customer type (Prospect and Customer). It holds the details such as, allowed customer types, allowed exit reasons. Further, it helps to reclassify a bank Rejected Prospect or Closed (Customer) back to its default or original status. |
| 29. | `COMPANY.CREATE` | Contains details, such as, Company's Name, Address, Mnemonic, Sub Division code, Creation Date and Default Company details. Allows user to create `COMPANY` record manually and from which data gets auto-populated in `COMPANY` application. |
| 30. | ST.CUSTOMER.CLOSURE.PARAM | Path to access the applicaiton: **Admin Menu** > **Framework Parameter** > **Customer and Address** > **Customer Setup** > **Customer Exit Status**. This parameter application is used to configure the following:  *Enable Customer Closure* - This field can be entered only in the `SYSTEM` record. The user can select the provided check box to enable the customer closure process and perform the pre-closure checks.  Define the pre-closure conditions - The Transact core and non-core applications that must be checked for the presence of the customer data before the customer is closed, can be defined as individual records in this table. The user can define the following attributes in these records where ID of the record will be populated with the application name.  *Application Access Type* - This field is used to define the method through which the customer can be identified in the records of the application specified in the ID. This field will have two options:   - Field - Denotes that the system must access a particular field of the application to identify the customer - ID - The system must use the ID of the record to identify the customer.   *Application Access Link* - The user can provide a field name that will be referred to identify the presence of the customer data. |

Customer related tables available in the model bank are given below:

| S.No. | Parameter | Description |
| --- | --- | --- |
| 1. | `TARGET` | Target codes defined in this table are assigned to Customer records in Temenos Transact to indicate how the customer fits in with the Bank's overall marketing strategy. |
| 2. | `CUSTOMER.STATUS` | Customer Status codes defined in this table are assigned to Customer records in Temenos Transact to classify the customers based on the criteria defined locally. |
| 3. | `RELATION` | Helps to specify the various types of relations that can exist between Customers and, or Person Entities. |
| 4. | `CUST.GROUP.PURPOSE` | Defines the rules for a Customer Group based on the purpose of the group. The rules include where the customer group can be used and how the customers and parties in the group can be stored. |
| 5. | `PARTY.RELATIONSHIP` | Used to define multiple relationships between customers. |
| 6. | `DEPT.LEVEL` | Contains the valid levels of departmental hierarchy that are permitted in the system. |
| 7. | `DEPT.ACCT.OFFICER` | Used to identify each Department and Account Officer in the bank by means of a code. Each Customer record has an Account Officer code assigned, which helps to generate the M.I.S reports at the Account Officer level. |
| 8. | `ST.CDM.PARAMETER` | Holds the parameter configurations for customer dormancy processing at the lead company level. |
| 9. | `ST.CUSTOMER.ACTIVITY.PARAMETER` | This is a Parameter setup table, which helps to maintain the data relation details for the applications and it is enhanced to configure Access Type and Link for Joint account holders as well.  - *JH.ACCESS.TYPE* - This field determines on how the application can be accessed to get the list of personal data for joint account holders. - *JH.ACCESS.LINK* - This field provides the link of accessing the application for personal data for joint account holders. |
| 10. | `COUNTRY.RULES` | Helps to define the country specific rules. |
| 11. | `ADDRESS.RULES` | Helps to define the country specific address rules for each country. |
| 12. | `COUNTRY.PARAMETER` | Helps to check the address rule that has to be applied to get the address details of the customer in a particular company. |
| 13. | `ADDRESS.OUTPUT.FORMAT` | Helps to define the various address output formats from which the user can choose the output formats. |
| 14. | `ADDRESS.OUTPUT.RULES` | Helps to define the Address Output Rules used for a country. |
| 15. | `CONTACT.TYPE.PARAMETER` | Helps the user to define the characteristics of each contact type captured in the `CUSTOMER` application. |
| 16. | `ST.REG.EXCLUDE.PARAM` | Exclusion Parameter setup is used to skip the customer activity.  - *PARTY.APPLICATION* – This field specifies the Party application for which the exclude criteria is going to define. (For now, this field is defaulted with 'CUSTOMER'). - *FIELD.NAME* –This field specifies the field name from the party application to define the exclude criteria. - *OPERAND* – This field specifies the operand that connects the field name and value. - *FIELD.VALUE* – This field specifies the value for the respective field name mentioned to define the exclude criteria. |

Interest related tables available in the model bank are given below:

| S.No. | Parameter | Description |
| --- | --- | --- |
| 1. | `BASIC.RATE.TEXT` | Defines descriptions of the Basic Interest Rate table IDs to enable the user to identify each one of them easily. |
| 2. | `BASIC.INTEREST` | Defines and stores the frequently used floating rates accessed by Temenos Transact applications when required. |
| 3. | `PERIODIC.INTEREST` | Defines the interest rates based on the time period for each currency. |
| 4. | `ST.PERIODIC.INTEREST` | Acts as an index for `PERIODIC.INTEREST`. This application can be either manually created or through the ST.CREATE.PERIODIC.INDEX service. |

## Illustrating Model Products

System table products available in the model bank are given below:

| S.No. | Products | Description |
| --- | --- | --- |
| 1. | `SECTOR` | - 141 – Common Sector - 1001 – Individual - 1002 – Staff - 1002 – Director - 2000 – Corporate - 3000 - Banks |
| 2. | `INDUSTRY` | - 1000 – Private Person - 1050 – Textile and Garments - 1200 – Staff - 1600 – Non Profit Institutions |
| 3. | `CATEGORY` | - 1000 – Demand Account - 1001 – Current Account - 1002 – CurrAcc with OD - 1003 – Premium C/A |
| 4. | `Exit Status` | The below values can be held for exit status field:   - Rejected - Deceased - Closed - Undesirable |