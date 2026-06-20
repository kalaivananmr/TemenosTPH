# Working with Account Creation

> Source: https://docs.temenos.com/docs/Solutions/T24_Transact/Accounts/AC/Accounts/AccountCreation/Working_With.htm

---

2. [Temenos Transact](../../../../content/T24_Transact.html)
3. You are here:
   Accounts > Account Creation > Working with

- Accounts;)
  - [Introduction](../../Accounts/Misc/Introduction.htm)
  - Account Creation;)
    - [Introduction](../../Accounts/AccountCreation/Introduction.htm)
    - [Configuration](../../Accounts/AccountCreation/Configuration.htm)
    - [Working with](../../Accounts/AccountCreation/Working_With.htm)
    - [Tasks](../../Accounts/AccountCreation/Tasks.htm)
    - [Outputs](../../Accounts/AccountCreation/Outputs.htm)
  - Account Maintenance;)
  - Account Limits;)
  - Account Interest and Charges;)
  - Locking of Funds;)
  - Notice Withdrawal;)
  - Savings Premium;)
  - Account Violations;)
  - Suspend Interest and Charges;)
  - Deferring Interest and Charges;)
  - Inactive Accounts;)
  - Posting Restriction;)
  - High Volume Accounts Processing;)
  - Account Funds Authorisation;)
  - Payment Netting;)
  - Account Passbook;)
  - Account Statements;)
  - Print Statement;)
  - CAMT Statements;)
  - Account Referral;)
  - Customer Standard Settlement Instructions;)
  - Generation of Scalable Account Numbers;)
  - NSF Exception Processing;)
  - Daylight Overdraft;)
  - Enhanced Transaction Search;)
  - Provider API for Account Balance Movements;)
  - Payment Currency Validation for Multicurrency Accounts;)
  - Account Closure;)

Temenos Transact

# Working with Account Creation

Updated On 07 September 2022 |  20 Min(s) read

Feedback
Summarize

The strength of Temenos Transact lies in the flexibility in which new account types can be created in order to meet the bank’s ongoing requirements. Once Temenos Transact is installed, part of the implementation process is to configure the types of accounts the bank wishes to offer and their characteristics. Typically, this includes:

- Debit or credit interest conditions.
- Interest and charges capitalisation frequencies.
- Statement production cycle.
- Other account group conditions.

Once these key files are setup, the creation of a new customer account is very simple.

## Customer Accounts

Follow the below steps to create or open a customer account:

1. The individual or corporate must be registered as a `CUSTOMER` of the bank. Temenos Transact is a customer orientated system. An account is connected to a CUSTOMER record and thus the owner and address details are not entered on the individual account.
2. The account must have an operating `CURRENCY` in which the balance is maintained.
3. The account is mapped to the appropriate banking product like:
   1. Savings Account (resident or non-resident)
   2. Current Account (simple or overdraft)
   3. Privilege Account (gold or silver)

This mapping is done through the `CATEGORY` and `ACCT.GEN.CONDITION` (grouping condition table).

For creating a basic customer account, the fields in `CUSTOMER`, `CURRENCY` and `CATEGORY` are mandatory. These are validated against the respective applications in Temenos Transact. Other than these fields, certain add-on fields are used to capture other relevant details pertaining to the account like:

- Mode of operation.
- Alternate account number.
- Interest liquidation mode.
- Event alert requirements.
- Mandates.

[Understanding Mode of Operation – Single or Joint](#)

An individual customer account is owned and operated in a single name or joint name. In case of joint account, each of the joint account holders must be registered as a customer of the bank. The relationship of main customer with the joint customer must be mentioned along with the documentary information (if any) about the joint holder. Signatures of the joint holder must be captured for verification. The joint holder relationship is one of the pre-defined values in the `RELATION` application in Temenos Transact.



[Understanding Mnemonic and Alternate Account Number](#)

Mnemonic is an alternate name for an account. The account can be referenced using the mnemonic across any Temenos Transactapplications, where the account number has to be used. The user can type the mnemonic and the system automatically fetches the corresponding account number while validating the application.

There is another concept similar to mnemonic. It is the alternate account number. In practice, where Temenos Transact has replaced an existing system, the system allows the access to customer accounts using the old account numbers for a short-term. Alternate account number feature was enabled to support this functionality. Later, this feature was extended to generate International Bank Account Number (IBAN) numbers when a new account is created. So, different alternate account numbers can be created for different purposes.

The nature and type of alternate account numbers are configured before the account is created. The parameters and applications related to alternate account number are as follows:

[ALT.ACCT.PARAMETER](#)

The structure of alternate account is defined and validated in this parameter application. It contains the following information:

- Account number type
- Check digit validation
- Minimum and maximum length of the alternate number
- Display mask



[ACCOUNT.PARAMETER](#)

If the bank wants to allow the users to reference the Temenos Transact accounts using the alternate account numbers, the *Alternate Acc Ids* field is set to Y and the applicable alternate account ID formats (defined in `ALT.ACCT.PARAMETER`) must be included in the *Alternate* *ID* field.

[ACCOUNT](#)

After configuring the `ALT.ACCT.PARAMETER` and `ACCOUNT.PARAMETER` applications, the user is allowed to capture the alternate account ID while creating an account. The alternate account type is defaulted from the `ACCOUNT.PARAMETER` application in the *Alt Acct Type* field. The user can capture the alternate account number, either manually or through an API using the *Alt Acct Id* field.



In the preceding screenshot, the user manually captures the alternate account ID for type LEGACY; whereas for type T24.IBAN, the system automatically generates the alternate account ID through an API that is linked.

[ALTERNATE.ACCOUNT](#)

This is an index application which stores the TTemenos Transact account number for the alternate account number. This is used for faster retrieval of the Temenos Transact account number when the alternate account number is used to refer other Temenos Transact applications.

[Extending the Length of Account Number Using Alternate Account Number](#)

The standard maximum length of account number is 16 digits. However, length of some of the alternate account types like IBAN is more than 16 digits. The `EB.OBJECT` application is configured to enable the extended alternate account number. For the ACCOUNT record in `EB.OBJECT`, the *Max Length* field can be defined with a value greater than 16 digits.

For example, if the user defines the *Max Length* field in `EB.OBJECT` as 36 characters, the *Alt* *Acct* *Type* in `ALT.ACCT.``PARAMETER` can be defined with the *Max Length* field upto 36 characters.



[Interest and Charge Liquidation Accounts](#)

The customer can instruct the bank to use one of his other accounts or group account for liquidating the interest and booking the charges, if any. Temenos Transact allows to define the interest liquidation account in any currency other than the account currency. The customer of the interest liquidation account can be different from that of the account customer. The customer can also specify which type of interest (CR/CR1/CR2/DR/DR1/DR2) they want to liquidate through the interest liquidation account. Some customers may opt to route the interest on their joint account to their savings account, while some customers may opt to route the interest on their account to their spouse’s account or kid’s account. The corporate current account holders may opt to route the interest to their funding account. Similarly, the account to which the charges are booked can also be different but the currency of the charge account must be the same as this account. The interest liquidation and charge liquidation accounts can be defined in the *Int* *Liqu* *Type*, *Int* *Liqu* *Acct* and *Charge* *Account* fields. The *Int* *Liq* *Ccy* is defaulted to the currency of account in *Int* *Liqu* *Acct* field.



[Changing the Main Customer in the Account](#)

There can be a requirement for the customer in an account record to be modified with that of another customer. For example, in case of death of the primary customer in an account record with the joint holder, Temenos Transact allows the modification of the main customer ID for an account record with *Joint Holder ID* to any one of the existing *Joint Holder ID* in the account record.

The system does not allow modification of the main customer if there are limits linked to the customer.

Modification of the main customer is validated against the `CATEGORY` range as defined in `ACCOUNT.PARAMETER` application in the SYSTEM record. The following screenshot shows the example setup of `CATEGORY` range in `ACCOUNT.PARAMETER`.



Modification of the main customer ID for an `ACCOUNT` record with a single holder is allowed only for nostro accounts, even if the nostro `CATEGORY` range is specified in the `ACCOUNT.PARAMETER` application.

[Generating Alerts Based on Events](#)

The customer can subscribe or unsubscribe for alerts, through SMS or e-mail or secure messages, for one or more events. The event may be pre-determined (like account getting overdrawn or customer address change) or time based (like, a loan maturing in nn days or repayment scheduled in nn days). The events can be initiated by the user or the system. The alerts can be activity alerts, transaction alerts, balance alerts, transfer alerts or portfolio alerts.

[Issuing Mandates](#)

The individual or corporate customer can issue mandates mentioning the details of the authorised signatories and their signing powers to approve transactions in specific currency and amount on behalf of the customer. This is recorded in `EB.MANDATE` application. Each of the authorised signatory must be registered as a customer in Temenos Transact and must be linked to the `EB.SIGNATORY.GROUP` with the details of currency and amount upto which they have the signing powers.



## Internal Accounts

Internal accounts can be opened manually or automatically. For certain types of internal accounts (like cash accounts, suspense accounts, inter-company accounts and AL currency position accounts), where the category is parameterised in the respective application, the system generates the accounts automatically.

It is recommended to create the internal accounts manually for the local currency accounts, based on which the system can automatically open any foreign currency account, as required. The accounts have to be manually created for the non-parameterised internal account categories like fixed or movable assets account.

The internal accounts are not customer based accounts and hence is not linked to any customer. The currency and category are defaulted from the ID of the account. For example, if the ID of the internal account is EUR1122100010001, the *Currency* field is defaulted to EUR and *Category* field is defaulted to 11221. Customer is not updated for internal accounts so it is mandatory to define the following fields while creating the account.

- *Account Title*
- *Short Name*
- *Mnemonic*
- *Account Officer*

The automatically created internal account has the text RECORD.AUTOMATICALLY.OPENED set in the *Account* *Title.1, Account* *Title.2* and *Short* *Title* fields. These can be amended later by the bank users. As the internal accounts are created and maintained for bank’s internal operations, the interest and charge conditions do not apply to them. Some internal accounts are used for special processing like inter-branch or inter-company accounts, position accounts and multi-GAAP accounts.

[Understanding Inter-Branch or Inter-Company Internal Accounts](#)

These accounts are used as parking accounts to perform the financial transactions on accounts belonging to a different branch or company. In this setup, each branch holds an inter-branch account with the other branch or branches or one branch is identified as the inter-company routing branch through which all the inter-branch transactions are routed. The routing branch details are defined in `INTERCO.PARAMETER` application. The format of the internal account differs according to the company setup.

In the case of multi-branch or multi-book setup, the format of inter-branch account is CCYCCCCCNNNNBBBB, where:

- CCY is the swift currency code of the account, for example EUR, USD.
- CCCCC is a category code defined in the INTERCO record of `ACCOUNT.CLASS` application.
- NNNN is sub division code (defined in the `COMPANY` application) of the other branch in the transaction.
- BBBB is the sub division code (defined in the `COMPANY` application) of the branch.

[Example](#)

The transaction is done in Branch A (sub division code 0004) for an account belonging to Branch B (sub division code 0008). The ID of the inter-branch account is USD1280000080004 for Branch A and USD1280000040008 for Branch B.

In the case of multi-company setup, the format of inter-company account is – CCYCCCCCNNNN, where:

- CCY is the swift currency code of the account, for example EUR, USD.
- CCCCC is a category code is defined in the `INTERCO` record of `ACCOUNT.CLASS` application.
- NNNN is the sub division code (defined in the `COMPANY` application) of the other company in the transaction.

The sub division code of Company A is 0002 and Company B is 0003. The format of inter-company account for Company B in Company A is USD128000003 and for Company A in Company B is USD128000002.

[Understanding AL Currency Position Accounts](#)

Banks can opt to capture the currency position movements for reporting purposes. This is done through the *Position**Entry* field in the `CONSOLIDATE.COND` application. If this field is set to `ACCOUNT`, the currency position movements are captured in the internal accounts based on the category defined for this purpose in the `EB.POSITION.PARAMETER` application.



In case of multi-book or multi-company setup, the format of currency position internal account is CCYCCYCCCCCDDSSBBBB, where:

- The first CCY is the currency code of the account.
- The second CCY is the other currency of the position relationship.
- CCCCC is a category code in the range 10000–19999.
- DD is the *Dealer**Desk* (default value is 00, captured from the `EB.POSITION.PARAMETER` application) for which the accounts are maintained.
- SS is a sequential number that allows access to sub account processing, if required
- BBBB is the sub division code of the company the account belongs to.

For CCYCCY, if the local currency is USD and there is a transaction in EUR, then two accounts need to be updated (EURUSD and USDEUR). The EURUSD account is the EUR account with the amount based on the sign of EUR in the transaction that updates the position. The USDEUR account is a local currency account with the opposite sign to that of the EUR.

[Example](#)

If the ID is EURUSD1902201030001, then:

- EUR is the currency code of the account.
- USD is the position relationship currency.
- 19022 is the category code.
- 01 is Dealer Desk
- 03 is the sequential number
- 0001 is the *Sub Division Code* of the company

In a single company setup, the format of currency position account number is CCYCCYCCCCCDDSS, where:

- The first CCY is the currency code of the account.
- The second CCY is the other currency of the position relationship.
- CCCCC is a category code in the range 10000 – 19999.
- DD is the *Dealer**Desk* (default value is 00, captured from the `EB.POSITION.PARAMETER` application) for which the accounts are maintained
- SS is a sequential number, which allows access to sub account processing.

If the ID is EURUSD190220103, then:

- EUR is the currency code of the account
- USD is the position relationship currency
- 19022 is the category code
- 01 is Dealer Desk
- 03 is the sequential number

[Understanding Multi-GAAP Accounts](#)

To setup multiple financial reporting in Temenos Transact, internal accounts are required. For example, IAS, IFRS or other forms of local reporting. To distinguish these accounts and their entries from other reporting systems, they must be setup with the appropriate *Position* *Type* (in the `CATEGORY` application) to match the reporting system defined in the `FX.POS.TYPE` application. The used for the internal account must have the correct *Position* *Type* value to match the reporting system.



## Nostro Accounts

The key of nostro accounts is similar to customer account. It is the shadow or mirror account of the vostro account maintained by the correspondent bank. So, the nostro Account is opened with the correspondent bank as the customer. For validating the nostro accounts, the NOSTRO record in `ACCOUNT.CLASS` application should be updated with the *Category* (marked for nostro accounts) and *Sector* (pertaining to corresponding banks).

The nostro account is identified based on the *Category* and *Limit Reference* field in the `Account` application. The system defaults the *Limit* *R**eference* field as NOSTRO, based on the setup in `ACCOUNT.CLASS`. These accounts are marked for reconciliation. The statements and advices to these accounts are re-directed to the nostro reconciliation department for reconciliation purposes.

The following screenshot shows a sample nostro account.



## Contingent Accounts

Banks, in certain cases, may have to maintain the balances of the off-balance sheet or contingent items for reporting purpose. To facilitate this, contingent accounts are created. These accounts are created for customer accounts or internal accounts. For example, contingent customer accounts are created for guarantees held. Posting to these accounts is done through the `DATA.CAPTURE` or `FUNDS.TRANSFER` applications of Temenos Transact. The category range for contingent accounts is defined in the `ACCOUNT.PARAMETER` application as shown in the following screenshot.



The customer contingent accounts are also used to capture the unutilised or utilised amount of the sanctioned limit on which the interest and charges are applied. The LIMIT record is monitored for changes and the unutilised or utilised amount is updated to the contingent account as and when the amount changes. Accounting entries are raised to show the movements from or to the contingent accounts. Internal contingent accounts are used to offset or balance the accounting entry movements to the customer contingent accounts.



The *Contingent Int* field is mandatory for setting up the contingent Account. This field denotes how the interest on the contingent account is treated in Temenos Transact. The following are the possible values in this field.

| Possible Values | Description |
| --- | --- |
| B | Indicates non-contingent interest to be reported in balance sheet. The interest and charge liquidation account needs to be a non-contingent account, in order to report the interest or charge as a balance sheet item. |
| C | Indicates contingent interest, which must not appear on the Balance Sheet. The interest or charge liquidation accounts can also be contingent accounts. |
| O | Indicates non-contingent interest but reported as an off balance sheet item. |
| I | Indicates an internal contingent account, which is used to counterbalance contingent accounts. This must not appear on the balance sheet |

[Sweeping of Unutilised/Utilised Limit Amounts](#)

The *Procs Limit Sweep* field in the `LIMIT.PARAMETER` application must be set to Y to enable the sweeping of unutilised or utilised limit amount into a contingent account. The *Allow Unutil Cr* field in the `LIMIT.PARAMETER` determines whether the unutilised portion of a partially utilised limit can be transferred to the contingent account. The *Default Max Total* field determines whether, the `INTERNAL.AMOUNT` or the `ADVISED.AMOUNT` of the limit is to be used for the calculation of unutilised limit amount.

The contingent account to which the sweeping of unutilised or utilised limit amount is specified in the *Unutil Acct* or *Util Account* fields in the `LIMIT` application. The current unutilised or utilised amounts are considered based on these fields. There is an option to override the `LIMIT.PARAMETER` application based on the setting of whether credits to the contingent account should occur when the unutilised amount is reduced. The following screenshot shows an individual `LIMIT` settings for contingent accounts.



The contingent accounts are updated at the end of day. The accounts can also be updated through the `DATA.CAPTURE` and `FUNDS.TRANSFER` applications. Funds transfer is possible only when both the accounts are non-contingent accounts or when both accounts are contingent. Similarly, in `DATE.CAPTURE``,` the entire batch must be of the same type.



In this topic

- [Working with Account Creation](#WorkingwithAccountCreation)

- [Customer Accounts](#CustomerAccounts)
- [Internal Accounts](#InternalAccounts)
- [Nostro Accounts](#NostroAccounts)
- [Contingent Accounts](#ContingentAccounts)


Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Friday, April 17, 2026 1:43:00 AM IST