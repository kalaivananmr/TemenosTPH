# Introduction to Fedwire Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Clearing_Non_Value_Messages/US/US_Clearing_Fedwire__PPFEDW/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Clearing Non Value Messages

- [Clearing Non Value Messages Clearing Non Value Messages](../../US/US_Clearing_Fedwire__PPFEDW/Introduction.htm)
  - [Introduction](../../US/Non-Value Messages/Introduction.htm)
  - [Configuration](../../US/Non-Value Messages/Configuration.htm)
  - [Working with](../../US/Non-Value Messages/WorkingWith_1.htm)
  - [Tasks](../../US/Non-Value Messages/Tasks.htm)
  - [Outputs](../../US/Non-Value Messages/Outputs.htm)

Payments

# Introduction to Fedwire Clearing

Updated On 22 March 2025 |
 9 Min(s) read

Feedback
Summarize

Fedwire is the USA’s interbank funds transfer system, which settles on gross basis in real time. The features of Fedwire are as follows:

- Processes domestic and cross-border payments in USD
- Handles payment individually as it is a Real-Time Gross Settlement (RTGS) system
- Processes unconditional payment orders one at a time automatically on a continuous basis. Thus, Fedwire provides immediate and final settlement of all payments, provided there are sufficient funds or overdraft facilities in the payer’s account.
- Uses proprietary network for message exchanges between participant banks and settlement system, and is a V-copy settlement.

## Types of Payment and Messages

Temenos Payments Hub (TPH) supports generation and processing of customer and bank-to-bank transfers, and provides the required information. The US Regional Layer (USMB) generates the outward clearing message, whereas the inward clearing message is received in USMB and passed to TPH. The below diagram explains the flow of messages between TPH bank and Fedwire, with TPH acting as a direct participant.

Boxes in green are Temenos systems.



- Payment can be as follows:
  - Initiated manually from an ordering bank (account holding institution)
  - Received as an instruction from the client (pain.001 file)
  - Entered by the back office user in the Order Entry (OE) page
- TPH bank (as originator) – Processes the request and generates an IF event to USMB, which sends the clearing message to Fedwire.
- Fedwire clearing – Sends the ack or nack to TPH bank, which is received by USMB and passed to TPH.
- TPH bank (as beneficiary) – Receives incoming payment message in TPH neutral file format.

## Payment Instruments

Fedwire is an RTGS system that supports only credit transfers.

## Routing Number

Fedwire uses ABA Fedwire Routing Number as the preferred bank or branch identification method. TPH supports storing of this number and is mandatory for the payment.

## Cut-Off Time

Fedwire’s cut-off times for customer and bank-to-bank payments are as follows:

- Opening of Fedwire Funds Service – 9:00 pm ET on the preceding calendar day
- Cut-off (Other than Settlement Payment Orders) – 6:00 pm ET
- Cut-off (Settlement Payment Orders) – 6:30 pm ET

## Outward Payment Processing

This section describes the outward processing of an order initiated in TPH bank.



| Activity | Description |
| --- | --- |
| Manual capture of Fedwire payment from branch or back office by using OE page | - Captures a Fedwire payment from TPH OE page. - Validates mandatory and non-mandatory fields on submission and displays an error (if any). |
| Payment instructions through ordering bank | Ordering party’s bank (same as TPH or another bank) sends payment instructions to TPH bank. The instruction can be in SWIFT MT or any ISO20022 format. |
| Account validations | Validates the following for ordering account:  - Is a valid Temenos Transact account - Has no posting restrictions - Has sufficient balance to cover the transaction |
| Business validations | Checks whether the instructed amount is empty. If provided, the currency needs to be in USD. |
| Balance check (not shown in diagram) | Checks whether the debit account has enough funds for the payment to be processed. If available, the funds are reserved. |
| Submission and supervisor approval | Performs the following validations:  - On submission, the payment waits for the Supervisor’s approval.   - If approved, it is moved for further processing.   - If rejected, it can be modified and resubmitted for approval. - Payment is then sent to Temenos Payments Engine for further processing.   Payments received in TPH from external banks in STP mode do not wait for supervisor’s approval. |
| Warehouse | Warehouses the payment with future execution date and releases on the SOD of the execution date. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement and needs to be performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the payment to a TPH clearing channel (FEDWIRE). If the system finds that the clearing cut-off is in past, the payment is routed through an alternate channel or warehoused by TPH to be released the next business day. Routing through an alternate channel is available only with Payments Hub (PH) license. |
| Dates calculation | Calculates the payment value and booking dates, which are configured to current date (similar to the execution date) |
| FX calculation | Applies when customer and payment account currencies are different. If FX shifts are involved, it adjusts the value date forward and warehouses the payment. This feature is only supported with PH license. |
| Balance reservation | Reserves funds on the debit account. This is done on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges. Charge mode can be BEN, SHA or OUR. |
| Duplicate check | Enables to configure checks on payment amount, currency, and transaction reference for payments received from an ordering bank.  To know more, refer to Duplicate Check section. |
| Posting | Debits the payment amount and charges to be borne by the customer to the debtor’s account. If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (such as automatic retry, reject or cancel).  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode - If AMS is external, then it generates posting request in a native XML format and accepts response from the external system.  Outward Payments  - Debit debtor account - Credit Fedwire clearing Nostro account.  Inward payments – Entries made when an inward message is received from USMB:  - Debit Fedwire clearing Nostro account - Credit customer account |
| Outward payment generation | Triggers an IF event, which generates TPH neutral format message for USMB and clearing message in Fedwire format |
| Error queue | If an error occurs while processing the Fedwire payment, it moves the transaction to the Error queue for the user to repair or cancel the payment. |

## Inward Payment Processing

This section describes the inward processing of a payment received from Fedwire, destined to an account in TPH bank.



| Activity | Description |
| --- | --- |
| Payment received from SWIFT network | Receives an inward payment from USMB in TPH neutral file format (originally from Fedwire) |
| Account validation | Validates the beneficiary account for the following:  - Sort code or account number unknown - Closed or stopped - Not in currency quoted |
| Bank code validation | Validates creditor BIC or code for an indirect participant |
| Dates calculation | Receives Fedwire payments with value date as current business date and processes the payment immediately |
| Filtering | Performs filtering of payments (if configured). This is a bank specific requirement and is performed in the site |
| Fee calculation | Applies only for customer transfers |
| Duplicate check | Performs on payments received from Fedwire for the configured set of payment attributes, such as payment amount, currency and transaction reference |
| Credit posting | Debits Fedwire clearing Nostro account and posts credit to the beneficiary account |
| Error queue | If an error occurs while processing the Fedwire payment, it moves the transaction to the Error queue for the user to repair or cancel the payment. |

- Non-value messages are not supported in TPH according to the list.
- Non-value messages has the following Business Function Code and Type or Sub Type Code:
  - Customer Transfer Plus – 1001 1501 1601 1007 1507 1607
  - Bank-to-Bank Drawdown Request or Response – 1631 1633
  - Customer or Corporate Drawdown Request or Response – 1031 1033
  - Service Message (SVC) – 1001 1501 1601 1007 1507 1607 1033 1590 1633 1090 1690

## Illustrating Model Parameter

To know more on parameter setup for Fedwire Clearing, refer to [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

US RTGS module can send and receive the real time gross settlement payments in the United States.

In this topic

- [Introduction to Fedwire Clearing](#IntroductiontoFedwireClearing)

- [Types of Payment and Messages](#TypesofPaymentandMessages)
- [Payment Instruments](#PaymentInstruments)
- [Routing Number](#RoutingNumber)
- [Cut-Off Time](#CutOffTime)
- [Outward Payment Processing](#OutwardPaymentProcessing)
- [Inward Payment Processing](#InwardPaymentProcessing)
- [Illustrating Model Parameter](#IllustratingModelParameter)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [Temenos Payments Hub](../../Payments_Hub_(PP)/Misc/Introduction.htm)
- [Payments Initiation](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm)
- [Temenos Payment Services](../../Services/Misc/Services.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 6:07:00 PM IST