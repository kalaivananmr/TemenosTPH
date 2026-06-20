# Introduction to Static Data

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Static_Data/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Temenos Payments Hub > Static Data > Introduction

- Temenos Payments Hub;)
  - [Introduction](../../Payments_Hub_(PP)/Misc/Introduction.htm)
  - [Messaging Framework Messaging Framework](../../Payments_Hub_(PP)/MessagingFramework/Introduction.htm)
  - Clearing;)
  - Sanction Screening;)
  - Status Reporting;)
  - Cheque Clearing;)
  - Code Words;)
  - Direct Debits;)
  - International Payments (MT);)
  - Manual Repair;)
  - Business Dates;)
  - Posting;)
  - Fees and Billing;)
  - Funds Reservation;)
  - Warehousing;)
  - Book Transfer;)
  - Investigations and Enquiries;)
  - Routing and Settlement;)
  - Business Validations;)
  - Static Data;)
    - [Introduction](../../Payments_Hub_(PP)/Static_Data/Introduction.htm)
    - [Configuration](../../Payments_Hub_(PP)/Static_Data/Configuration.htm)
    - [Working with](../../Payments_Hub_(PP)/Static_Data/Working_with.htm)
    - [Tasks](../../Payments_Hub_(PP)/Static_Data/Tasks.htm)
    - [Outputs](../../Payments_Hub_(PP)/Static_Data/Outputs.htm)
  - Standalone Payments;)
  - [Standalone Implementation Options Standalone Implementation Options](../../Payments_Hub_(PP)/Standalone_Implementation_Options/Standalone_Implementation_Options.htm)
  - Forex;)
  - Bulk Payments;)
  - Bank Condition;)
  - Client Condition;)
  - Product Determination;)
  - Housekeeping Functions;)
  - FATF and WTR2;)
  - PSD2;)
  - SWIFT gpi;)
  - SWIFT Universal Confirmations;)
  - Instant Payments;)
  - Agency Banking;)
  - Returns and Reversal;)
  - Exceptions and Investigations;)
  - Clearing Status Report;)
  - Monitoring;)
  - Counterparty Risk;)

Payments

# Introduction to Static Data

Updated On 12 April 2026 |
 21 Min(s) read

Feedback
Summarize

Temenos Payments Hub module uses the following static data records for end-to-end processing of the payments received from customers, payment channels, PAYMENT.ORDER (PO) application or bank channels.

## Company Properties

Financial institutions can process payments in their branches across different geographical locations. Temenos Payments Hub refers these branches as companies and maps it to the PP.COMPANY.PROPERTIES table for any setup that can process payments. Company properties are defined for each company, which needs to be valid in the system table (`COMPANY`) in Temenos Payments Hub.

1. To view the table, go to **Admin Menu** > **Payments** > **Payment Hub** > **Bank System Administration** > **Static Data** > **Company Properties**.
2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *HomeCountryCode* | Country code in ISO format |
   | *HomeCurrencyCode* | Currency code in ISO format |
   | *CompanyRegion* | Region of the company |
   | *CompanyBIC* | Bank Identifier Code (BIC) of the company |
   | *TimeZone* | Time zone of area (continent) or location (city) |
   | *Enable FATF Reg* | Financial Action Task Force (FATF) regulation for payment transactions |
   | *National Clearing System Code* | National Clearing Code (NCC) used to derive a BIC from an IBAN |
   | *EnableCustomerGrouping* | Indicates whether the customer grouping feature is to be applied to the Client Agreements and Client Charges screens.  If this field is set, the customer group defined in Charges and Fees (CG) module can be defined in the *Business Line / Customer Group* field in the Client Agreements and Client Charges screens.  If this field is not set, then the customer target is stored in the *Business Line / Customer Group* field in the Client Agreements and Client Charges screens. |
   | *Skip BIC/Bank Code Validation* | Indicates if:  - the BIC and Bank Code validations against the SWIFT Bank Directory in the Centralised Payment Reference Directory module are performed or not during payment capture and payment STP processing. - the BIC validations are performed while creating or updating TPH configuration tables. If the checkbox is selected, the aforementioned validations are not performed. If the checkbox is not selected, the aforementioned validations are executed accordingly. |
   | *CNY TO CNH Conversion Required* | Determines whether CNY to CNH currency conversion is required. If checked, automatically converts Payments, Non-Payment messages received in CNY into CNH currency. |
   | *Allowspecialcharacterset* | Indicates whether the special characters set is allowed in the outward/ redirected payment messages.  - Set as Y if the bank supports special character set. If the value is Y, then the system uses code page ID configured in the *Code Page Set* field in the table to validate the special characters. - If left blank (default), the system does not support special character set. In such cases, the system validates against ASCII.VAL.TABLE with key STANDARD.SW. The system determines whether special character set has to be supported in the following sequence for outgoing or redirected payments,  - If the *Allowspecialcharacterset* field is set to N in PP.BANK.CONDITION table, the system validates against ASCII.VAL table with key STANDARD.SW. - If the *Allowspecialcharacterset* is left blank in PP.BANK.CONDITION, the system validates against company properties for the receiving bank BIC or sort code. Codepageset - Configure the ID of the code page against the special characters to be validated.  The configured Codepageset should be a valid record in ASCII.VAL.TABLE |

## Currency

Temenos Payments Hub allows payment transactions in different currencies. It refers to the PP.CURRENCY table in payments hub, which lists all currencies along with the conversion rates that can be transacted for each company. Currency needs to be a valid record defined in the PP.CURRENCY table. Additionally, other currency attributes are defined in the PP.CURRENCY table that are specific to Temenos Payments Hub.

1. To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Currency**.
2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Currency Code* | Two-character unique country code |
   | *Currency Name* | Name of the currency |
   | *Fractional Digit* | Fractional digit for the currency |
   | *Charge Fractional Digit* | Fractional digit of the currency considered for charges. If the user does not configure this field, the value in the *Fractional Digit* field is used for charges. |
   | *Country Name* | Country to which the currency belongs |
   | *Exotic Currency* | Thinly traded currency |

A customer debiting payment in EUR and with transaction currency RSD (defined as exotic) enables payment to be routed to a EUR correspondent bank.

## Region

Temenos Payments Hub groups countries in different regions using the PP.REGION table in payments hub. It is used to differentiate the holidays applicable for different regions within a country to calculate different value dates. For example, regions within a country can have different holidays.

- To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Region**.

## Source

Temenos Payments Hub can find the origin (internal or external) of a message in payments hub using the PP.SOURCE table. It is referred by components, such as product determination, client condition and client charges.

1. To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Source**.
2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Channel Name* | Channel through which messages are received |
   | *Source Product* | Group to which the source belongs |
   | *Source Type* | Source of payment for Temenos Payments Hub, such as: - Client channel – Payments from customer channels or IP - Non-client channel – Payments from Clearing - Internal channel – Internal payment |

## Channel

Temenos Payments Hub finds the origination channel through which incoming and outgoing payments are routed for processing using the PP.CHANNEL table. It is the logical name assigned to a physical queue, and more than one queue can be configured to a single channel.

- To view the table, go to **Admin Menu** > **Payments** > **Payment Hub** > **Bank System Administration** > **Static Data** > **Channel**.

## Error Types

Temenos Payments Hub triggers different error types when there is an error, warning or information during payment processing in payments hub.

- To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Error Types**.

## Clearing Non-Working Day

Temenos Payments Hub determines clearing-specific holidays based on the region of a Country Code before clearing any payments using the PP.CLEARING.NONWORKINGDAY table. This table is referred during payment processing to determine various attributes of the payment such as Dates, Clearing Settlement process and Routing and Settlement.

- To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Clearing Non-Working Day**.

## Currency Non-Working Day

Temenos Payments Hub determines the currency holidays while processing payments using the PP.CURRENCY.NONWORKINGDAY table. This is referred by Dates component while calculating various value dates in that particular currency.

- To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Currency Non-Working Day**.

## Party Role

Temenos Payments Hub defines various debit and credit party roles for a payment based on the SWIFT or ISO20022 message tags by using the PP.PARTY.ROLE table.

- To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Party Role**.

## Status Code

Payments in Temenos Payments Hub go through various stages during processing:

- Define three digit numerical status codes to identify each stage. These status codes are hardcoded.
- To find the current status of the payment, refer to the PP.STATUS.CODE table.

To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Status Code**.

## Program Characteristic

The PP.PROGRAM.CHARACTERISTIC table helps Temenos Payments Hub to perform the following:

- Find the program invoked for monitoring payments.
- Check whether payments has reached the status defined for the record.

It is a client-specific table used to send status information to client’s `TRIP` application (Track and Trace mechanism responsible for informing different client channels about the payments statuses).

To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Program Characteristic**.

## Weight Assignment

Temenos Payments Hub can find the special processing rules applicable for a payment based on the high, medium or low weights assigned to it by using the `WEIGHT ASSIGNMENT` table. Apart from these basic weights, there can be specific user-defined weight codes assigned to the payment (such as enabling or disabling certain functionalities to optimise its processing in payments hub).

- To view the table, go to **Admin Menu** > **Payment Hub** > **Weight Assignment**.

The debit account balance check for an outgoing direct debit payment can be skipped based on the specific weight code as it is not relevant.

## Programs Per Weight

Temenos Payments Hub can decide whether the following components (such as balance check, bank condition, client condition, filtering, and duplicate check etc.) needs to be executed or not for a payment by using the PP.PROGRAMS.PER.WEIGHT table:

This helps in reducing or optimising the processing time of the payment.

- To view the table page, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Programs Per Weight**.

## Component API Hook

Temenos Payments Hub can configure APIs that enable user-defined handling of restrictions on accounts and values dates using the PP.COMPONENT.API.HOOK table. This API hook can also be used to change the credit account of a payment based on a user-defined logic.

The system can change or impose the *Processing Date*, *Credit Value Date* and *Debit Value Date* fields according to the user-defined rules determined by API. This API hook can also be used to change the credit account of a payment, for instance, based on a user defined logic.

There are two types of API hooks:

- PRE API Hook – Performs the changes to the values as explained above
- POST API Hook – Validates the payment and triggers errors or warnings based on the user-defined rules.

To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Component API Hook**.

## Transaction Types

Temenos Payments Hub can define different transaction types (such as Credit Transfers, Direct Debits, Credit Transfer Returns, Direct Debit Reversals, Clearing Status Report and Resolution of Investigation) to denote the exact flow of the payment or message. During the mapping exercise, each payment message type can be allocated to a specific transaction type, which is a valid record in the PP.TRANSACTION.TYPES table. These transaction types are used in different functionalities, such as Product Determination, Clearing Settings and Value Dates.

- To view the table, go to **Admin Menu**>**Payment Hub**>**Static Data**>**Transaction Types**.

## In Channels

Temenos Payments Hub can find the Inward Queue name from where the payment messages are received from clearing, client or internet banking by using the PP.IN.CHANNELS (inward framework component) table.

- To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **In Channels**.

## Source Setting

Temenos Payments Hub can find various non-clearing or client sources from which payments are received. Additionally, it checks whether the customer status report to be generated for the particular source of payment by using the PP.SOURCE.SETTING table.

1. To view the table, go to **Admin Menu** > **Payment Hub** > **Static Data** > **Source Setting**.
2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Transaction Type* | Transaction type for which the record is created, such as: - CT – Credit Transfer - RT – Return Credit Transfer |
   | *Message Payment Type* | Message type of the payment. The value links to the *Message Payment Type* field in PP.MSGPAYMENTTYPE or PP.MSG.FORMAT tables. The default value is "\*".  The user can enter values in the below subsequent fields only when a message type is specified (for example, pain.001 or pain.008).  - *Batch Fee Hold Indicator* - *Max Allowed days* - *Cust Status Rpt on Settlement* - *Customer Status Report Returns* - *Customer Status Report Rejects* - *Automated Cancel Indi* If the user enters the full message version (for example, pain.001.001.09 or pain.008.001.08) in *Message Payment Type* field, the system does not allow the user to enter values in the above-mentioned fields. |
   | *Cust Status Rpt on Settlement* | Whether to generate customer status report for each received and processed initiation file, where the settlement date of the bulks in the file is equal to the current business date. |
   | *Max Allowed Days* | Number of maximum allowed days to process the payment, beyond which the application warehouses parent transaction. This is applicable only for Direct Debit Initiations. |
   | *Customer Status Message Type* | Customer status message type for which the user creates the record.  This field holds the name and format of the status report message that the system must generate and send to the submitter of original transaction. Value in this field can either be a message type (for example, pain.002) or a full message version (for example, pain.002.001.10).  This is mandatory when the user enters any of the below fields.  - *Cust Status Rpt on Settlement* - *Customer Status Report Rejects* - *Customer Status Report Returns* |
   | *Customer Status Report Rejects* | Customer Status Report (CSR) generated for rejected transactions during payment origination, such as:  - EoD – CSR is generated during end of day process - Immediate – CSR is generated immediately as part of payment processing - Blank – CSR is not generated |
   | *Customer Status Report Returns* | Customer status report generated for return transactions during payment origination, such as:  - EoD – CSR is generated during end of day process - Immediate – CSR is generated immediately as part of payment processing - Blank – CSR is not generated |
   | *Identity Comparison* | Indicates whether an identity check (Name Comparison) should be applied on the inward payment messages. Possible values: Yes or Blank |
   | *Name Check Amount Limit* | Indicates the transaction limit beyond which the TP invokes the BNC for an inward payment. Currency of the amount range is always in local currency of the company. If the transaction currency is different from the local currency then a mid-rate is used to convert the transaction amount to the local currency amount  *Name Check Amount Limit* set in a Clearing record in SOURCE.SETTING applies for all Clearing Transaction type and Message Type listed in the record. |
   | *Score Percentage* | Indicates the tolerance to scoring similarity and can be used only when *Name Check Amount Limit* is used. If left blank, score for the limit is consider as 100%  *Score Percentage* set in a Clearing record in SOURCE.SETTING applies for all Clearing Transaction type and Message Type listed in the record. |

Read [Configuring Static Data](Configuration.htm) for more information on how to configure enhance Beneficiary Name Comparison feature in TPH.

## Authorisation Principle

Temenos Payments Hub uses the PP.AUTHORIZATIONPRINCIPLE table to determine the levels of authorisation required (when manually authorising a payment). This table is viewed for the following scenarios:

- Cancelling a payment from a Warehouse queue
- Authorising a payment from the following:
  - Order Entry (OE) page
  - General Repair queue
  - Direct Debit queue
  - Cheque Debit queue

1. To view the Authorisation Principle page, go to **Admin Menu** > **Payment Hub** > **Authorisation Principle**.
2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Status* | Payment status for which the authorisation principle record is created |
   | *Direction* | Direction (Book, Incoming, Outgoing or Redirected) of the payment message for which authorisation principle record is created |
   | *Authorisation Principle* | Number of authorisations required for a payment (for 4 or 6 eye authorisation) |

## BIC and NCC

Temenos Payments Hub can store the BIC and NCC by using the centralised Reference Data module.

- BICs are stored in the Central Bank Directory
- NCCs are stored in Central Bank Directory and the IBAN Plus tables.

[RD.CENTRAL.BANK.DIR](#)

This table holds the following details:

- BIC (BIC 8 or BIC 11) of the correspondent banks
- National identifier code
- Address of the institutions



During payment processing, when the NoBicBkCdValidation checkbox is not selected in both the Company Properties table and Clearing Configuration table (used for configuring the channel through which the payment is routed), this RD.CENTRAL.BANK.DIR table is referred to perform the following:

- Validate the BIC and bank codes
- Derive the BIC from bank code and vice versa

Refer to the [Centralised Reference Data](../../../../../T24_Transact/Framework/RD/CRD/Misc/Introduction.htm) guide in Banking Framework for more information.

[IN.IBAN.PLUS (IBAN Plus Directory)](#)

This table has the following:

- *Iban Bic*
- *Routing* *Bic*
- *Iban* *National* *Id* of the correspondent



## IBAN Structure Directory

The IN.IBAN.STRUCTURE record has the following:

- IBAN structure (IS Files) information downloaded from the Swift Directories
- Length of IBAN
- Position identifiers for bank, branch and BIC.



## SWIFT Directory Create and Maintain

Refer to [BIC and Bank Code](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/International_Payments/Configuration.htm#BICandBankCode) to create and amend Central Bank Directory.

## IBAN Plus Exclusion Directory

The IN.EXCLUSION.LIST displays the IBAN NATIONAL identifiers, which are not allowed in IBANs. To know more, refer to Product Features and Deal Processing in Banking Framework.

The upload mechanism to this directory is centralised in the common Reference Data (RD) module. To know more on the upload process, refer to [Centralised Reference Data](../../../../../T24_Transact/Framework/RD/CRD/Misc/Introduction.htm) in Banking Framework. The below screenshot displays the IN.EXCLUSION.LIST table.



## Multi Company and Multi Book Support

Temenos Payments Hub provides a complete enterprise solution to support global banks with separated business rules and segregated data. A headquarter company is defined at the highest level with multiple country level companies and branches within the country (if required). All the payment transaction and static data within Temenos Payments Hub are associated with a company. The company data is managed using the data visibility mechanism (restricts the user to view data for defined company or companies) and user application rights (restricts the user to use system functions). Companies can also be configured to share data with each other, which allows common set of users to manage payments for a group of companies.



Transfers initiated with debit and credit account that belongs to:

- Different companies is knows as inter-company transfers. For example, transfer from an account in branch 1 (MF2) of lead company MF1 to an account in lead company SG2.
- Different branches in the same company is known as inter-branch or multi-book transfers. A branch can also be a lead company itself. For example, transfer from an account in branch 1 (MF2) to branch 2 (MF3) in the same lead company MF2.

## PP.ERRORTYPES

This application is used to configure error messages of type WARNINGS and INFORMATION in Payments Hub. An error can be configured as a warning or error in this application.

## PI.ISO.EXTERNAL.CODE

This application is used to configure an ISO external code list published by ISO Registration Authority. The PP.ORDER.ENTRY,PAYMENT.ORDER and EB.QUERIES.ANSWERS (EBQA) application screen used for initiation of Investigation Request (camt.110) refers to this table to display the values for the below fields when the user initiates the ISO payment / investigation request from payment / investigation request initiation screens.

- *Service Level Code*
- *Local Instrument Code*
- *Category Purpose Code*
- *Transaction Purpose Code*
- *Organization Other Identification Scheme Code*
- *Private Other Identification Scheme Code*
- *Referred Document Information Type (for structured Remittance Info)*
- *Clearing System Identification Code*
- *External Account Identification Code*
- *Investigation Type Code <InvstgtnTpCd>*
- Investigation Sub Type Code <InvstgtnSubTpCd>
- Investigation Reason Sub Type Code <RsnSubTpCd>

The above codeset is the ID of the PI.ISO.EXTERNAL.CODE table.

Either the system can automatically or the user can manually upload the values for these codesets using Temenos Transact upload service (T24.UPLOAD.PROCESS). The user can also manually add, edit, or delete the values from this table. Any manual update for the codes in the table is overwritten during the next automatic or manual upload if there are any changes existing for that code in the latest file.

While manually adding or editing the code value, the user must enter ‘Code Value – Code Description’ in the *Code Description* field since ISO OE initiation screen displays the value only from the *Code Description* field.

In this topic

- [Introduction to Static Data](#IntroductiontoStaticData)

- [Company Properties](#CompanyProperties)
- [Currency](#Currency)
- [Region](#Region)
- [Source](#Source)
- [Channel](#Channel)
- [Error Types](#ErrorTypes)
- [Clearing Non-Working Day](#ClearingNonWorkingDay)
- [Currency Non-Working Day](#CurrencyNonWorkingDay)
- [Party Role](#PartyRole)
- [Status Code](#StatusCode)
- [Program Characteristic](#ProgramCharacteristic)
- [Weight Assignment](#WeightAssignment)
- [Programs Per Weight](#ProgramsPerWeight)
- [Component API Hook](#ComponentAPIHook)
- [Transaction Types](#TransactionTypes)
- [In Channels](#InChannels)
- [Source Setting](#SourceSetting)
- [Authorisation Principle](#AuthorisationPrinciple)
- [BIC and NCC](#BICandNCC)
- [IBAN Structure Directory](#IBANStructureDirectory)
- [SWIFT Directory Create and Maintain](#SWIFTDirectoryCreateandMaintain)
- [IBAN Plus Exclusion Directory](#IBANPlusExclusionDirectory)
- [Multi Company and Multi Book Support](#MultiCompanyandMultiBookSupport)
- [PP.ERRORTYPES](#PPERRORTYPES)
- [PI.ISO.EXTERNAL.CODE](#PIISOEXTERNALCODE)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 2:54:45 PM IST