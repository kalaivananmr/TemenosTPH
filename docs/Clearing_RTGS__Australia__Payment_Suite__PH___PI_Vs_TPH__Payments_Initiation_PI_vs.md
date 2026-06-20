# Payments Platform Standard (PP)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Australia/Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm

---

2. [Payments](../../../../content/payments.html)

- Australia;)

Payments

# Payments Platform Standard (PP)

Updated On 07 August 2025 |
 13 Min(s) read

Feedback
Summarize

Payments Platform Standard is a lightweight, entry-level payment solution designed for processing core client payments—both domestic and international—with low transaction volumes and support for up to three clearing systems (such as ACH, SEPA, RTGS, or Cheque Clearing). It offers only the bare minimum features required for payment processing, including basic payment enrichment and rule-driven execution. With limited configurability and scalability, it is best suited for institutions with straightforward payment needs. This solution is exclusively available in embedded mode with Temenos Core Banking.

In contrast, Enterprise Universal Payments is a comprehensive, enterprise-grade payment hub built for high-volume, complex payment processing. It supports various payment types, including high-value, batch, and instant payments, all configurable through parameterization—eliminating the need for software modifications. It is designed for scalability and flexibility, consolidating multiple payment systems into a single, streamlined solution. Unlike Payments Platform Standard, it minimizes manual intervention, enhances operational efficiency, and supports both embedded deployment with Temenos Core Banking—a key differentiator of the Temenos offering—or standalone integration with an external Demand Deposit Account (DDA) or account management system



## Ready Reckoner to Features in Payments Platform Standard vs Enterprise Universal Payments

| Feature | Payments Platform Standard | Enterprise Payments Hub |
| --- | --- | --- |
| Universal payment process (maximise STP rates) | No automated exception handling | ü |
| Stand-alone processing | Only embedded | ü |
| Intelligent routing | - Supports channel validations, reachability check, and directory upload - Does not support dynamic routing | ü |
| Advanced payment monitoring | Pending and processed payments monitor | Enhanced monitoring including cut-off time monitor, virtual queue monitor, etc. |
| Automated rate request to Treasury | On FX threshold breach, rate needs to be entered manually. | ü |
| Automated return handling | û | ü |
| Funds Check | - Park the funds for manual action - Retry using recycler - Park in repair when rejected by department account officer | Automatic cancellation when rejected by department account officer |
| Trigger auto investigation messages | û | ü |
| Agency banking | û | ü |
| Corporate customer agreements | û | ü |
| Automated cancel of payment initiations | û | ü |
| Group claims | Only supports individual claims | ü |
| Refund of direct debits | û | ü |
| Value dates for return payments | û | Use value dates (original payment) |
| Automated negative response to payment recall | û | ü |
| Expiry of unanswered recalls | û | ü |
| Acceptance of customer initiated recall | û | ü |
| Advanced option for filtering response handling | û | Automatic return, cancel or seize funds |
| Define cut-off time based on payment currency | û | ü |
| Non STP rules for customer and bank transfer for correspondent banks | û | ü |
| Warehouse payments from correspondent banks | û | ü |
| Customer or customer group specific statement formats | û | ü |
| Customer or customer group specific non STP rules | û | ü |
| Customer or customer group special instructions for statements | û | ü |
| Customer or customer group specific lead times for cut-off | û | ü |
| Risk filtering | û | ü |

## Features

The following are the features available:

| Features | Description | | | |
| --- | --- | --- | --- | --- |
| Universal Payment Process (maximise STP Rates) | Handles the following payment types in a single workflow:  - High care (SWIFT or RTGS) - Low care (ACH) - Single - Batch - Normal - Urgent - Instant   Enables centralisation of payments in a single payment engine and determines the payment product based on the following:   - Payment attributes – *Source/Channel*, *Message Type*, *Urgency*, *Currency*, *Amount*, *Destination*, etc. - Pre-agreed client or bank agreements   Triggers the appropriate processing of SLAs, routing (clearing or correspondent to send the payment), pricing, booking and confirmations | | | |
| Restricted support in PP | | Processes different payment types in a single system along with the following restrictions:   - No support for instant payments - No automated exception handling to maximise STP - No dynamic routing and settlement - Restricts volume to 500K per annum - Supports up to three clearings | |
| Supported in PH | | Processes all payment types in a single system with the following supporting features:   - Can process instant payments with 24/7 processing and real time connectivity to clearing - Dynamic routing between different payment types - Automated exception handling to maximise STP - No restriction on volumes - Design to handle large volumes | |
| Stand-Alone Processing | Executes payments with accounts residing in an external Core Banking System (CBS) or DDA. The system communicates with an external CBS or DDA by using asynchronous messages. - It needs to be deployed with Temenos Infrastructure (TI) - It is only supported with PH. | | | |
| Intelligent Routing | Enables definition of routing rules to determine the correspondent or clearing using which the payment needs to be sent. Routing can be based on message priority.  - High priority payments can be sent using urgent channels or clearings. - Instant payments are routed using instant clearing channel.   Channel validations, reachability check and directory support are performed as part of routing. The following are the available routing options:   - Loro or Nostro (preferred correspondent, SSI or agent) - RTGS clearing channel - ACH clearing channel - Instant payment clearing channel - SWIFT payments using Serial or Cover method   Allows to define multiple routing options and select appropriate route. If a payment misses the cut-off or the channel cannot be reached, the following options are available:   - Next available channel - Warehouses and processes the payment on the following day - Processes on the same day with a shift in value date - Checks for a country level routing definition, when the current routing definition is at party level - Parks the payment in repair | | | |
|  | Restricted support in PP | Does not support dynamic routing of automatically selecting the appropriate channel (based on reachability, cut-off time, routing to instant payments clearing). If the payment misses cut-off or the chosen channel is not reached, it routes the payment to repair. Allows only ‘BNK’ (bank) level contract definition. Channel validations, reachability check, and directory support are available. | | |
| Advanced Payment Monitoring | Allows payments in different statuses to be monitored easily and to take appropriate action. Different types of payment monitors are available in the system:  - **Pending or processed transactions** – All payment transactions in different statuses - **Process monitor** – Count of payments in process or flight by status - **Virtual queue monitor** –   - Payments in virtual queues (soft definition)   - Multiple queues can be brought in a single virtual queue monitor - **Cut-off time monitor**   - Payments awaiting currency or channel cut-offs with the expiry or cut-off time   - It can be further customised to raise alerts based on cut-off times | | | |
|  | Restricted support in PP | | | Supports only pending or processed transactions. |
| Automated Rate Request to Treasury | FX processes foreign currency payments with conversions using real time rates. Real time rates can be entered from Temenos CBS or any external DDA or rates system. Payments breaching currency threshold can be sent to FX dealer:   - To provide the treasury rate - To automatically process using the rate provided   Additionally, it is sent to the manual repair queue for an operator to enter the treasury rate. FX rates can be imposed by an operator in Manual Order Entry and Repair pages. Payments can be processed by taking input of a pre-approved deal rate (by imposing the deal rate). | | | |
|  | Restricted support in PP | | | - Supports FX conversions with real time rates. The Operator can override the FX rates. - Payments breaching threshold can be parked in the manual repair queue for operator to enter the rate. |
| Automated Return Handling | Can return a payment (credit transfer, direct debit, cheque) received from clearing exceptions (such as invalid or missing account, missing or invalid mandate, restrictions on the account, insufficient funds, and screening failure). | | | |
|  | Restricted support in PP | | | - Can auto-return a payment for exceptions (such as invalid or missing account or invalid or missing mandate) - It routes the payment to repair, for all other exceptions. |
| Funds Check | If funds are unavailable, the system routes the payment to one of the following: **Manual action** – The Department Account Office performs the below actions.   - Approves the overdraft - Approves once the funds are available - Rejects the payment If rejected from the Manual Action queue based on the configuration, it routes the payment to repair, or cancels or returns it automatically. - Sends to recycler to retry for funds | | | |
|  | Restricted support in PP | | | If payment is rejected, it parks the payment in manual repair queue. |
| Triggering Auto Investigation Messages | Auto-triggering of investigation messages (Pacs.028) to ascertain status of the payments, when conformation is not received from clearing.  It is only supported in PH. | | | |
| Agency Banking | Receives and forwards the payment or file from or to Indirect Participants (IP). It is available only with PH. | | | |
| Corporate Customer Agreements | When a payment batch (credit or debit) is initiated by a corporate customer and the payments within the batch fails, it is routed to repair.  - If it is rejected (credit or debit), an option is available to create a consolidated reject report to customer (Pain.002) on settlement date or certain days (configurable) after the settlement date.   When a payment (single or batch) is initiated by a corporate customer, the user needs to defines the following:   - Number of days post (requested) collection date on which the system needs to perform funds check (for a book direct debit) - Number of days post settlement date on which customer status report needs to be generated (pain.002) | | | |
| Automated Cancel of Payment Initiations | Auto-cancel payment initiations from customers (credit transfers, direct debits) for exceptions (such as invalid or missing account, restrictions on the account, insufficient funds, and screening failure). | | | |
|  | Restricted support in PP | | | Routes the payment to repair for all other exceptions. |
| Group Claims | Supports both the bank claims (individual and group). | | | |
|  | Restricted support in PP | | | Supports only individual claims. |
| Refund of Direct Debits | Allows a refund for a direct debit which is paid based on an authorised or unauthorised mandate. It is only supported in PH. | | | |
| Value Dates for Return Payments | Imposes the value date for a return payment to be the same as the original payment. It is only supported in PH. | | | |
| Automated Negative Response to Payment Recall | Negative response for a cancellation request can be automatically sent when the original transaction is not found or cancellation request is received after cut-off days. | | | |
|  | Restricted support in PP | | | Response to a recall request is manual. |
| Expiry of Unanswered Recalls | Defines the number of days within which the incoming cancellation request needs to be accepted from the date of original settlement or the system marks it as overdue. It is only supported in PH. | | | |
| Acceptance of Customer Initiated Recall | Defines the number of days within which the incoming customer initiated cancellation request needs to be accepted from the date of original settlement. It is only supported in PH. | | | |
| Advanced Option for Filtering Response Handling | Payments that are screened for (AML check) and if the response is a hit, the following options are available:  - Seize funds in an inward credit transfer - Auto cancel, return or reject payment - Park for manual action | | | |
|  | Restricted support in PP | | | Allows only to park for manual actions. |
| Define Cut-off Time Based on Payment Currency | Defines cut-off times for a channel based on currency of the payment.  It is only supported in PH. | | | |
| Non-STP Rules for Customer and Bank Transfer for Correspondent Banks | Allows to set non-STP rules to park payment for manual intervention, for customer and bank transfers received from specific correspondent banks. It is only supported in PH. | | | |
| Warehouse Payments from Correspondent Banks | Enables warehousing for customer and bank transfers received from specific correspondent banks. It parks the payments in warehouse until the requested execution date or credit value date. It is only supported in PH. | | | |
| Customer or Customer Group Specific Statement Formats | Defines specific statement formats for a customer or group of customers. It is only supported in PH. | | | |
| Customer or Customer Group Specific Non STP Rules | Payments processed for a customer or group of customers can be made non-STP based on their configuration. It is only supported in PH. | | | |
| Customer or Customer Group Special Instructions for Statements | Defines special instructions to be sent when producing account statements for customer or group of customers. It is only supported in PH. | | | |
| Customer or Customer Group Specific Lead Times for Cut-off | Defines lead times to be used while arriving at the cut-off time for channel, customer or group of customer. It is only supported in PH. | | | |
| Risk Filtering | Performs country, currency, counter party and transaction amount limit. It is only supported in PH. | | | |

In this topic

- [Payments Platform Standard (PP)](#PaymentsPlatformStandardPP)
  - [Ready Reckoner to Features in Payments Platform Standard vs Enterprise Universal Payments](#ReadyReckonertoFeaturesinPaymentsPlatformStandardvsEnterpriseUniversalPayments)
  - [Features](#Features)

Related topics:

- [Temenos Payments Hub](../../Payments_Hub_(PP)/Misc/Introduction.htm)
- [Temenos Payment Services](../../Services/Misc/Services.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Wednesday, June 17, 2026 2:23:36 PM IST