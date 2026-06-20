# Introduction to Client Conditions

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Client_Condition/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Temenos Payments Hub > Client Condition > Introduction

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
  - Standalone Payments;)
  - [Standalone Implementation Options Standalone Implementation Options](../../Payments_Hub_(PP)/Standalone_Implementation_Options/Standalone_Implementation_Options.htm)
  - Forex;)
  - Bulk Payments;)
  - Bank Condition;)
  - Client Condition;)
    - [Introduction](../../Payments_Hub_(PP)/Client_Condition/Introduction.htm)
    - [Configuration](../../Payments_Hub_(PP)/Client_Condition/Configuration.htm)
    - [Working with](../../Payments_Hub_(PP)/Client_Condition/Working_with.htm)
    - [Tasks](../../Payments_Hub_(PP)/Client_Condition/Tasks.htm)
    - [Outputs](../../Payments_Hub_(PP)/Client_Condition/Outputs.htm)
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

# Introduction to Client Conditions

Updated On 23 May 2023 |
 25 Min(s) read

Feedback
Summarize

A bank processes payment transactions for clients (both retail and corporate) by using different options, products, and services. It can customise various services or products to suit the customer requirements. The customer can choose from a predefined set of options that allows to define their choices and agrees with the services availed from the bank.

The client condition functionality of Temenos Payments Hub can create different client products with various customer preferences for their payment processing. These conditions are checked for all payments where the ordering or beneficiary client has an account with the Temenos Payments Hub bank and not a financial institution. Bank conditions are not required for all types of messages and is controlled by the weight assigned for the payment. The users can configure a program for each weight to skip the client condition check. The below table shows an example of client conditions for different types of transactions.

| Payment Types | Client Condition Debit Party Role | Client Condition Credit Party Role | Comments |
| --- | --- | --- | --- |
| Customer Transfer (CTR) outgoing | Ordering party | NA |  |
| Book transfer | Ordering party | Beneficiary party |  |
| Incoming CTR (on-us) | NA | Beneficiary party |  |
| Outgoing local clearing settlement transaction | Debit party- Internal suspense account(for that clearing) | Credit party - Clearing Nostro account | Book payment |
| Outgoing local clearing individual payment (outgoing CTR) | Ordering party | Credit party internal suspense account for that clearing |  |
| Incoming local clearing settlement transaction | Debit party - Clearing Nostro account | Credit party - Internal suspense account for that clearing | Book payment |
| Incoming bulk local clearing individual payment (incoming CTR) | Debit party – Internal suspense account for that clearing | Beneficiary party |  |
| Parent of logical batch | Ordering party (default parent) | Credit party - Internal suspense account | Book payment |
| Child of logical batch | Ordering party (copied from parent) | Beneficiary Party (if on-us) and NA (if off-us) | Outbound or book payment |

## Client Condition Product

The bank sells their services to its customers. A service or a combination of services can be packaged as a product. Each payment product has certain characteristics, such as:

- Domestic or international payment
- Customer or bank transfer
- High or low value payment
- Urgent or normal payment

A client using multiple payment products wants different set of conditions for each product to enable flexibility. Additionally, when a payment falls within the PSD regulation (for example, payments in EU-EEA currency, and originating or terminating in EU-EEA country), certain rules are applied. The product determination considers characteristics before arriving at a product, hence, the product output is taken as input for deciding the conditions to be applied for the payment.

## Client Agreement

A bank deals with the following clients:

- Retail
- High Net Worth Individual (HNI)
- Corporates

The bank can customise the services specifically for each client. The following sub-categories are available within the above-mentioned categories:

| Category | Description |
| --- | --- |
| Business Line or Customer Group | Each client segment can have certain banking preferences that influence payments processing. The conditions set at this level provides consistent industry, business line, or customer group specific processing options.  In Temenos Payments Hub, customers are grouped based on the *EnableCustomerGrouping* field in the COMPANY.PROPERTIES table.   - When this field is disabled, the customers are grouped based on the *Company ID*, *Client Condition Product*, *Source Product*, *Business Line* (Customer Target), *Client ID*, *Account Number* and *Account Currency* fields in CLIENT.CHANGERS. - When this field is enabled, in addition to the fields mentioned above, customers can be grouped using the entire set of attributes associated to each customer. The grouping rules can be defined as per the requirement and these rules can be attached in CLIENT.AGREEMENTS and CLIENT.CHARGES. The ability to apply the entire set of customer related fields to group the customers is possible only when the customer data is present in the Temenos Payments Hub database (Temenos Payments Hub can be in the embedded mode or in the standalone mode, but customer data is replicated) and a client ID is associated to the account.   Refer to the [Customer Groups](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Client_Condition/Configuration.htm#CustomerGroups) section in the [Configuring Client Conditions](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Client_Condition/Configuration.htm) topic for more information. |
| Client ID | Client conditions can be setup on a client ID level. This functionality allows for similar processing of all payments for a particular client ID. There can be multiple accounts tagged to a single ID, hence, the similarity allows to track the processing options easily. This is client specific and customisable than the conditions set in the business line. |
| Client Accounts | Client agreements are defined at the account-currency level (for a single client) and along with product (if required). This makes it a specific agreement at the product, client ID, account or currency level. Additionally, it allows to setup granular level conditions that are special for a particular account. Client agreement has the following attributes:   - Input – To configure client conditions and are matched while processing payments. - Output – To influence the payment processing and apply on the best-matched client condition (identified by payment engine). |

## Client Condition for Batch Payments

Temenos Payments Hub checks whether the payment is a single payment or part of a batch (parent or child) to apply client condition. In batch payments, the client condition is determined for the parent (which is then applied to the child transactions).

[Define Client Condition](#)

Temenos Payments Hub defines the client conditions by using input attributes. Each condition is created for a specific Temenos Transact company. The users can create multiple client conditions by using various combination of the input attributes (from high-level generic condition to client specific condition). The following are the important input attributes:

| Field | Description |
| --- | --- |
| *Client Condition Product* | Output from the product determination component. |
| *Source Product* | Single product can be attached to multiple sources.  Bank can have different client conditions for different sources or one condition for source group to which all the actual sources belong. |
| *Business Line / Customer Group* | Defines the client’s business line or customer group. Customer grouping can be switched on or off from the COMPANY.PROPERTIES table. When customer grouping is switched off, this field is used to define the customer’s business line (target from CUSTOMER application).  When switched on, this field stores the customer group. Customer groups can be defined using all field in the CUSTOMER application. The grouping rules can be defined as per requirement and these rules can be attached in the CLIENT.AGREEMENTS and CLIENT.CHARGES tables. The ability to apply the entire set of customer attributes to group customers is possible only when customer data is present in the Temenos Payments Hub database (Temenos Payments Hub is in embedded mode or in standalone mode, but customer data is replicated).  Refer to the [Customer Groups](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Client_Condition/Configuration.htm#CustomerGroups) section in the [Configuring Client Conditions](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Client_Condition/Configuration.htm) topic for more information. |
| *Client* *ID* | Each client has a client ID defined within the customer and account database. During payment processing, it is retrieved based on the account. |
| *Account Number* | Account number to be debited or credited based on the payment or client instructions. |
| *Currency* | Currency of the account for which client conditions needs to be determined. This is retrieved from the account and customer database, based on the account number. |

## Payment Processing Using Client Condition Output

Bank conditions are defined in Temenos Payments Hub for each company by using various combination of input attributes. When a payment is processed, the payment engine compares the payment data against the configured client conditions. It attempts to find the best matching client condition by using peeling-off mechanism.

- If a match is found, the payment engine extracts the various output client conditions and applies it on the payment for client specific processing.
- If a match is not found, it applies the default client condition.

The output attributes of client conditions can influence the following payment processing features:

[Value Added Tax (VAT) or Tax on Transaction](#)

VAT is a form of consumption tax that the government collects on services and products offered to customers. VAT value is stored as percentages and used by the fee and posting components of Temenos Payments Hub. The following are the two types of VATs:

| Type | Description |
| --- | --- |
| VAT on transaction amount | VAT on principal amount |
| VAT on charges | Indicates whether VAT is applied on the charge |

During payment processing, fee component performs the VAT calculation. Similarly, Temenos Payments Hub can configure tax details for processing.

[Advice or Confirmations to Clients](#)

This includes the communication that a client receives from the bank that inform about their transactions. Temenos Payments Hub can process the following confirmations types:

| Confirmation Type | Description |
| --- | --- |
| Phone Confirmation | Payments that are important for clients or require immediate and updated information. In this case, a client can receive a call from the bank to inform them about the status of the transactions. |
| SMS or Email Confirmation | A confirmation from the bank about the status of the transactions for various payments. |
| Debit Advice or Credit Advice | SWIFT messages related to an account that a corporate client can receive from the bank.  - MT900 is a confirmation of debit - MT910 is a confirmation of credit |
| Printed advice by Delivery | Printed statements or advices of all transactions for recording and reconciliation of their accounts through Delivery (DE) module Advice Print service. Clients migrating from funds transfer to TPH can have print advice posted through DE which is currently used by funds transfer application.  Delivery module will be present along with PP or PH module when TPH is deployed as standalone system. Delivery print service can be used to generate print advices in standalone architecture even when customer details are not replicated in TPH and also not available in Party MS. |
| Printed advice by Post | Printed statements or advices of all transactions for recording and reconciliation of their accounts through the Autoform application. |
| Fax confirmation | Fax confirmations for payment transactions. |

It also allows the user to configure specific advices or confirmations that needs to be sent to clients for transactions on their account by using client condition output.

[Transaction Types Applicable for Print Delivery Method](#)

Confirmations through DE PRINT Service is sent for the following transaction types in TPH only when the print confirmation is configured or enabled for the payment type.

| Payment Type | TPH Clearing Transaction Type | Advice Type (Debit/Credit) |
| --- | --- | --- |
| Incoming Credit Transfer | CT or Blank | Credit Advice |
| Outgoing Credit Transfer | CT or Blank | Debit Advice |
| Book Credit transfer | CT or Blank | Debit and Credit Advice |
| Incoming Direct Debit | DD | Debit Advice |
| Outgoing Direct Debit Collection | DD | Credit Advice |
| Incoming return of outgoing CT | RT | Credit Advice |
| Outgoing return of incoming CT | RT | Debit Advice |
| Incoming return/refund of outgoing direct debit | RF/RD | Debit Advice |
| Outgoing return/refund of incoming direct debit | RF/RD | Credit Advice |
| incoming reversal of incoming direct debit | RV | Credit Advice |
| Outgoing reversal of outgoing direct debit Collection | RV | Debit Advice |
| Reversal of previous credit transfer | CT or Blank | Credit Advice |
| Reversal of previous Debit transfer | CT or Blank | Debit Advice |
| Incoming cheque debit /drafts from clearing | CD | Debit Advice |
| Draft issue from payment order | CD | Debit Advice |

The system releases one print debit advice and one print credit advice format for all the payment types. Clients are allowed to configure or format the print advice details based on their requirements.

The print advice is generated when,

- print processing is enabled for the payment type and source (configured in the PP.PROGRAMS.PER.WEIGHT table for specific and high-level weight of the payment)
- configured in client condition

[Separate Booking Charges](#)

A client can choose how the charges needs to be displayed in their periodic statements. When charges are not posted in a separate account, clients can book them together with the main amount or separately. Posting scheme considers this while processing the transactions.

[Example](#)

A customer makes a foreign payment of $1000 from the account. Assuming that the bank has a policy of charging such transactions at a flat rate of $15. The following is the difference in entries

|  |  |  |  |
| --- | --- | --- | --- |
| Book Together | Dr | Client | $1015 |
| Cr | XYZ | $1000 |
| Cr | Bank P&L | $15 |
| Book Separately | Dr | Client | $1000 |
| Dr | Client Charges | $15 |
| Cr | XYZ | $1000 |
| Cr | Bank P&L | $15 |

Temenos Payments Hub can achieve the separate charge posting functionality by using the client condition output.

[Detailed Booking Charges](#)

If charges are posted separately, clients prefer to have the detailed break-up of all the charges in their statements or as a lump sum amount. This requirement can arise due to reconciliation. Temenos Payments Hub can achieve this detailed charge posting functionality using the client condition output.

If a payment falls in Payment Services Directive (PSD), charges needs to be booked separately and a break-up is provided to the clients. A book separate option is available for all PSD products and the Operator needs to be informed to setup the client conditions.

[Example](#)

A customer makes a foreign payment for $1000 from the account. The total amount of charges is $100 (Charge1 = $60, Charge2 = $40).

|  |  |  |  |
| --- | --- | --- | --- |
| Post summary of Charges | Dr | Client | $1000 |
| Dr | Client Charges | $100 |
| Post Charges in Detail | Dr | Client | $1000 |
| Dr | Client Charges 1 | $60 |
| Dr | Client Charges 2 | $40 |

[Separate Charge Account](#)

Clients prefer to maintain a separate account for all charges incurred while using the bank’s services. This special charges account can be listed in client condition, hence, fees and posting components can book all charges in that account.

This feature is available only when the client conditions are defined at a client ID or account level, though different accounts can be provided for debit and credit side. Charge account can be defined for a specific transaction currency or applicable for all currencies. Currency conversion happens when charge account currency is different from the transaction currency. The charge account is uniquely identified by company, account or currency.

[Example](#)

Client A prefers to pay charges from the main transaction account. Client B prefers to pay charges from the special charges account setup for paying charges. Therefore, the entries for the same type of transaction for the two clients appear as given below.

Assuming that the transaction amount is $1000 and charges are $15.

|  |  |  |  |
| --- | --- | --- | --- |
| Charges from the Transaction Account for Client A | Dr | Transaction Account | $1015 |
| Cr | XYZ | $1000 |
| Cr | Bank P&L | $15 |
| Charges from a Separate Account for Client B | Dr | Transaction Account | $1000 |
| Dr | Spl Charge Account | $15 |
| Cr | XYZ | $1000 |
| Cr | Bank P&L | $15 |

The Operator can impose a charge account for a party (debit or credit) by using Order Entry (OE) or Repair page, when the party is a client of the processing company. If imposed, the charge account defined in the client conditions record must not override the imposed charge account available in the payment order.

[Straight-Through Processing (STP)](#)

STP refers to the complete payment processed electronically without any manual intervention or information entered by the bank operator. Some clients prefer this, whereas, others have their transactions monitored by an Operator during processing (which results in moving the payment to Non-STP). This can be chosen at the client condition level and considered while payment processing.

If non-STP is chosen, the payment is routed to Manual Repair queue.

The correct currency account is not chosen automatically for some clients, and requires the Operator to call the customer to confirm the credit account or currency. In this case, the transaction is a non-STP.

[Lead Time](#)

The bank configures lead time to ensure operations can successfully process the payment by using a channel, before reaching its actual cut-off time. The clients can negotiate with the bank about the lead time before the external cut-off time.

|  |  |
| --- | --- |
| Bank | Wants to have a larger lead time to manage operations smoothly. |
| Customer | Wants to have shorter lead times to manage getting higher number of payments processed in the available time frame. |

- Dates component of Temenos Payments Hub considers it for incoming or book payment.
- Routing and Settlement (R&S) component of Temenos Payments Hub considers it for redirect or an outgoing payment.

Lead time is subtracted from the cut-off time along with R&S lead time, making the actual cut-off (also known as internal cut-off time) earlier in the day. R&S considers this in an account to calculate the cut-off times. If lead time is not mentioned (including wildcard record) in client condition, the channel cut-off time (along with R&S lead time) is applicable.

Assuming channel specific cut-off time is 17.00 and client negotiated lead time is 0.5 hours. The last payment that the client can send for a day is at 16.30. All the payments after cut-off time are processed as received after cut-off time for that channel.

[Language](#)

Every client can have a language preference to receive alerts, confirmations, and advices for the payments. This can be used for language specific statement lines and charge descriptions in statement lines.

The client in UK (where the default language option is English) can choose to receive statements in any other language that Temenos Transact offers.

[Statement Format ID](#)

Every posting entry is associated with a description of the transaction, which is known a Statement format. The descriptions can vary depending on the level of detail that is available. Different clients can have customised statement formats for their debit and credit side transactions.

Assuming that there are two types of statement formats: 1 and 2.

Statement format 1 is attached to the posting line in the posting record, which gives information on payment currency and company code. Whereas, the client chooses the statement format 2 that gives information about payment currency, company code and amount in local currency.

[FX Discount](#)

All clients can negotiate a discount on the spreads, which the bank charges on the exchange rate for FX transactions. Client condition can store the negotiated discounts for the respective clients, which can be maintained currency-wise. The FX module reads the configured discounts and applies it during payment processing.

[Example](#)

A client who deals in three currencies can have the following discounts stored (value in percentage):

| Currency | Discount |
| --- | --- |
| EURO | 25% |
| USD | 70% |
| GBP | 15% |
| Wildcarded (\*) | 10% |

[Floats](#)

The processing time of transactions enables the bank that has money to use, in earning interest. Additionally, it can be defined as the difference between the debit and credit value date. The following are the two types of floats:

- Debit side (refers to debiting the customer)
- Credit side (refers to crediting the customer)

A client can choose to have floats in a transaction, which results in lower fees. Dates component uses this information for processing payments. For example, a client negotiates to have two days float on the debit transactions and one day float on the credit transactions.

If payment falls in PSD, it implies that floats are not taken on transactions.

[Billing Indicator](#)

Some banks have a separate billing engine that allows calculation of charges. Using client condition, the *B**illing* *I**ndicator* can be set to inform payment processing engine that the customer wants the payment module components to send the information to the billing engine and process the charges.

[Special Instructions](#)

When a payment falls in repair, the Operator is instructed to perform certain actions based on the client’s choice. This feature is available when the conditions are defined at the client ID or account level. It can be configured for both debit and credit side payments as *Debit Special Instructions* and *Credit Special Instructions*. For example, client can be informed about any FX transaction that goes to Non-STP.

[Non-STP for FX Transactions](#)

This specifies whether Operator review is required for transactions received in currencies (other than the credit or debit account currency). It allows for manual intervention and confirms posting of an FX transaction by the client. For example, a client has a Euro account and wants an intimation before any payment involving FX is processed on the account.

[FX STP Limit](#)

Configure an amount limit in home currency for FX transactions, when STP processing is configured in client condition. It moves all the FX transactions above the limit (set in the base currency of the bank) to manual repair.

The mid-rate identifies the limit, when the transaction currency is different from the base currency.

A client wants to move all FX transactions above €2000 to NSTP for Dollar CCY account.

## Client Conditions for International Financing Payments

International financing is a process in which a bank grants an advance (for example, loan set up where the funds are disbursed and recovered later) materialized by a financing line to its customer. It consists of setting up a loan or borrowing from treasury and trading room in return for interest over a determined period.

The following are the two possible scenarios in international financing payments:

- International financing involves releasing funds in an intermediary account (generally an internal account) and issuing an international transfer from this intermediary account while applying the pricing conditions of the ordering customer.
- Alternately, performing an international transfer can be based on a rate negotiated with another local bank. When a customer in the Temenos Payments Hub bank negotiates a rate with another local bank, the bank feeds their correspondent with the foreign currency amount and expects to receive a domestic transfer in the local currency from the Temenos Payments Hub bank. In this scenario, the system debits a transit account (Nostro) but applies the charge on the actual customer account based on the configured client charge for that customer.

In both the above mentioned scenarios, Temenos Payments Hub captures the payment leg where the debit main account is an internal or Nostro account. Generally, to lookup the account to be charged for the payment, the system reads the client conditions for the debit main account record. However, for international financing payments, the system reads the client conditions for the internal or Nostro account number entered in the *Debit Main Account* field but updates the charge account with the account number entered in the *Ordering Account* field. This is because the debit main account is an internal or Nostro account for an international financing payment but charges have to be applied based on the agreement with the original ordering customer.

If a payment has all the below characteristics, then it is identified as international financing payments:

- Payment is a customer transfer
- Payment direction is outgoing
- Payment is a non-batch payment
- Debit charge account is neither defined manually nor imposed during payment capture
- Debit main account is an internal or Nostro account
- Ordering account is present and different from the debit main account

In this topic

- [Introduction to Client Conditions](#IntroductiontoClientConditions)

- [Client Condition Product](#ClientConditionProduct)
- [Client Agreement](#ClientAgreement)
- [Client Condition for Batch Payments](#ClientConditionforBatchPayments)
- [Payment Processing Using Client Condition Output](#PaymentProcessingUsingClientConditionOutput)
- [Client Conditions for International Financing Payments](#ClientConditionsforInternationalFinancingPayments)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 2:55:26 PM IST