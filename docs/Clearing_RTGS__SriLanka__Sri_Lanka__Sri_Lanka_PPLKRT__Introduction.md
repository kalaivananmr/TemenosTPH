# Introduction to Sri Lanka RTGS Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/SriLanka/Sri_Lanka/Sri_Lanka_PPLKRT/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Sri Lanka > [Sri Lanka Clearing](../../Sri_Lanka/Sri_Lanka_PPLKRT/Introduction.htm) > Introduction

- Sri Lanka;)
  - [Sri Lanka Clearing Sri Lanka Clearing](../../Sri_Lanka/Sri_Lanka_PPLKRT/Introduction.htm)
    - [Introduction](../../Sri_Lanka/Sri_Lanka_PPLKRT/Introduction.htm)
    - [Configuration](../../Sri_Lanka/Sri_Lanka_PPLKRT/Configuring.htm)
    - [Working with](../../Sri_Lanka/Sri_Lanka_PPLKRT/Working_with.htm)
    - [Tasks](../../Sri_Lanka/Sri_Lanka_PPLKRT/Tasks.htm)
    - [Outputs](../../Sri_Lanka/Sri_Lanka_PPLKRT/Outputs.htm)
  - [Sri Lanka Cheques Sri Lanka Cheques](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Introduction.htm)
  - [Sri Lanka Interbank Payment System Sri Lanka Interbank Payment System](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Introduction.htm)
  - [Sri Lanka CEFTS Instant CT Payments Sri Lanka CEFTS Instant CT Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Introduction.htm)
  - [Sri Lanka CEFTS Instant DD Payments Sri Lanka CEFTS Instant DD Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Introduction.htm)

Payments

# Introduction to Sri Lanka RTGS Clearing

Updated On 22 March 2025 |
 8 Min(s) read

Feedback
Summarize

Sri Lanka RTGS is a SWIFT FIN copy-based Real Time Gross Settlement (RTGS) Clearing. It involves both inward and outward processing, (MT103 and MT202) with ‘LKB’ as the service identifier for the clearing. MT102 is handled as a part of this clearing.

## Sri Lanka RTGS Participants

Direct member is a participant bank that exchanges payments directly with Sri Lanka RTGS Clearing and holds a settlement account in RTGS.

## Types of Payment and Messages

Sri Lanka RTGS clearing supports the following message types:

| Message | Description |
| --- | --- |
| MT103 | Single customer credit transfer |
| MT202 | Financial institution transfer |
| MT102 (only incoming) | Multiple customer credit transfer |

The message flow between Temenos Payments Hub (TPH) bank and Sri Lanka RTGS Clearing is shown below.



1. User can initiate payment through the following sources:

- `PAYMENT ORDER (PO)` application
- Customer channels

2. TPH processes the payment, debits the ordering customer and sends an MT103 or MT202 to the Sri Lanka RTGS Clearing in a SWIFT format.
3. On receipt of the payment, the Sri Lanka RTGS Clearing performs the following:

- Settles the payment
- Forwards it to the receiving participant bank

4. At the receiving bank, TPH accepts the payment and performs validation and credit posting.

## Outward Payment Processing

This section describes the outward processing of an order initiated in TPH bank.



| Activity | Description |
| --- | --- |
| Manual capture of Sri Lanka RTGS clearing payment from branch or back-office using `PO` application or Order Entry (OE) page | Captures a Sri Lanka RTGS Clearing payment from `PO` application or TPH OE page.  - Any error encountered during validations of fields (mandatory and non-mandatory) are displayed on the page   To know more on Sri Lanka RTGS Clearing manual capture, refer to Manual Actions section. |
| Payment instructions through ordering bank | Sends payment instructions to TPH bank. The instruction can be in SWIFT MT format. |
| Account validations | Validates whether the ordering account has posting restrictions and sufficient balance to cover the transaction. |
| Bank code validations | Validates BIC against SWIFT BIC directory (if the directory is loaded and the system is configured to validate bank code). |
| Balance check | Checks whether the debit account has enough funds to process the payment. If available, the funds are reserved. |
| Submission and Supervisor approval | The user needs to perform the following:  1. On submission of the payment, it waits for Supervisor’s approval. 2. Once approved, payment is moved for further processing.  - If the Supervisor rejects the payment, it is modified and resubmitted for approval.  3. Payment is then sent to TPH for further processing.   Payments received from external banks in STP mode do not wait for Supervisor’s approval. |
| Warehouse | Warehouses the payments with future execution date. These payments are then released on the SOD of the execution date |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is bank specific requirement that is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the payment to a TPH clearing channel (LKB), which is configured to route to Sri Lanka RTGS Clearing through SWIFT network. Clearing channel determines the message type (MT103 or MT202) based on whether it is Customer or Bank Transfer If system finds that the clearing cut-off is past for Sri Lanka RTGS Clearing, TPH warehouses the payment for releasing it on the next business day. |
| Dates calculation | Calculates the payment value date and booking date, which are configured to current date (same as execution date) |
| Balance Reservation | Reserves funds on the debit account. Balance reservation is done on the payment amount with charges  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system |
| Fee calculation | Calculates the applicable charges for the payment. Charge mode is always set as Shared (SHA). |
| Duplicate check | Performs the check on payment amount, currency, and transaction reference for payments received from an ordering bank. |
| Posting | Debits the payment amount and charges to be borne by the customer to the debtor’s account. If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (such as automatic retry, reject or cancel).  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system  **Outward Payments** Entries made before sending MT103 or MT202 to Sri Lanka RTGS Clearing.  - Debit Debtor Account (or ordering bank account) - Credit Sri Lanka RTGS Clearing Nostro Account.  **Settlement Booking Entry** Processing the Sri Lanka RTGS Clearing payments credits or debits the clearing Nostro directly. There is no separate settlement processing and hence no settlement accounting for Sri Lanka RTGS Clearing payments. |
| Outward payment generation | Generates MT103 or MT202 message and parks the payment in ‘Awaiting acknowledgement’ status.  - Sri Lanka RTGS Clearing payments can be recognised by the service-code value (LKB) available in Field 103 of Block 3 of the SWIFT message |
| Error queue | If any error occurs during processing, it moves the payment to Error queue for the user to repair or cancel the payment. |

## Inward Payment Processing

This section describes the inward processing of a payment received from Sri Lanka RTGS Clearing, destined to an account in TPH bank.



| Activity | Description |
| --- | --- |
| Sri Lanka RTGS Clearing Payment received from SWIFT network | Receives an inward payment (MT103, MT202 or MT102) from Sri Lanka RTGS Clearing (through SWIFT network or SWIFT gateway) |
| Account validation | Validates the beneficiary account for the following:  - Beneficiary account number unknown - Beneficiary account closed - Beneficiary account stopped - Account is not in currency quoted |
| Bank code validation | Validates the creditor BIC code |
| Dates calculation | Receives Sri Lanka RTGS Clearing payments with value date as current business date, or future credit value date are processed immediately with the respective credit value dates |
| Filtering | Performs filtering of payments (if configured). This is a bank-specific requirement and is performed in the site |
| Fee calculation | Applies only for customer transfers The charge bearer is defaulted to SHA. |
| Duplicate check | Performs the check on payments received from Sri Lanka RTGS Clearing for the configured set of payment attributes, such as payment amount, currency and transaction reference. This can be performed in the site. |
| Credit posting | Debits Sri Lanka RTGS Clearing Nostro account and posts credit to the beneficiary account (59A). **Inward Payments** Entries made when an MT103 or MT202 is received from Sri Lanka RTGS Clearing.   - Debit Sri Lanka RTGS Clearing Nostro Account - Credit Customer account   Entries made when an MT012 is received from Sri Lanka RTGS Clearing.   - Debit Sri Lanka RTGS Clearing Nostro Account - Credit Batch Suspense Account   Following are the entries made for individual credits:   - Debit Batch Suspense Account - Credit individual customer account in tag 59.   **Settlement Booking Entry** Processing Sri Lanka RTGS Clearing payments credits or debits the clearing Nostro directly. There is no separate settlement processing and hence no settlement accounting for Sri Lanka RTGS Clearing payments. |
| Error queue | If any error occurs during processing, it moves the payment to Repair queue where user can repair or cancel the payment. |

In this topic

- [Introduction to Sri Lanka RTGS Clearing](#IntroductiontoSriLankaRTGSClearing)

- [Sri Lanka RTGS Participants](#SriLankaRTGSParticipants)
- [Types of Payment and Messages](#TypesofPaymentandMessages)
- [Outward Payment Processing](#OutwardPaymentProcessing)
- [Inward Payment Processing](#InwardPaymentProcessing)

Related topics:

- [Temenos Payments Hub](../../Payments_Hub_(PP)/Misc/Introduction.htm)
- [Payments Initiation](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm)
- [Temenos Payment Services](../../Services/Misc/Services.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:44:02 PM IST