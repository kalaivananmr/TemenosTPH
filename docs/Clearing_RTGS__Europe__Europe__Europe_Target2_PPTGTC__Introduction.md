# Introduction to TARGET2 Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_Target2_PPTGTC/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [TARGET2 Clearing](../../Europe/Europe_Target2_PPTGTC/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
  - [Swiss Interbank Clearing Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
  - [SEPA Instant Clearing-EBA INST SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
  - [SEPA Credit Transfer SEPA Credit Transfer](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Introduction.htm)
  - [SEPA Direct Debit SEPA Direct Debit](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Introduction.htm)
  - [TARGET2 Clearing TARGET2 Clearing](../../Europe/Europe_Target2_PPTGTC/Introduction.htm)
    - [Introduction](../../Europe/Europe_Target2_PPTGTC/Introduction.htm)
    - [Configuration](../../Europe/Europe_Target2_PPTGTC/Configuration.htm)
    - [Working with](../../Europe/Europe_Target2_PPTGTC/Working_with.htm)
    - [Tasks](../../Europe/Europe_Target2_PPTGTC/Tasks.htm)
    - [Outputs](../../Europe/Europe_Target2_PPTGTC/Outputs.htm)
  - [EPC SEPA Credit Transfer EPC SEPA Credit Transfer](../../Europe/EPC_SEPA_Credit_Transfer/Introduction.htm)
  - [EPC SEPA Direct Debit EPC SEPA Direct Debit](../../Europe/EPC_Direct_Debit/Introduction.htm)
  - [RPS German Cheque Processing RPS German Cheque Processing](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Introduction.htm)
  - [VIBER Payments VIBER Payments](../../Europe/Europe_VIBER_Payments_PPVIBR/Introduction.htm)
  - [MAV Payments MAV Payments](../../Europe/Europe_MAV_Payment_PPCLIT/Introduction.htm)
  - [Equens SEPA Direct Debit Equens SEPA Direct Debit](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Introduction.htm)
  - [Equens SEPA Credit Transfer Equens SEPA Credit Transfer](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Introduction.htm)
  - [TARGET2 Clearing (ISO20022) TARGET2 Clearing (ISO20022)](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Introduction.htm)
  - [Nordic Credit Transfer Payments Nordic Credit Transfer Payments](../../Europe/Europe_NCT_Payments_PPNPCT/Introduction.htm)
  - [Nordic Instant Credit Transfer Nordic Instant Credit Transfer](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm)
  - [Euro Swiss Interbank Clearing Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Introduction to TARGET2 Clearing

Updated On 22 March 2025 |
 14 Min(s) read

Feedback
Summarize

The second-generation Trans-European Automated Real-time Gross Settlement Express Transfer System (TARGET2) is the Eurosystem’s interbank funds transfer system. This is designed to support the objectives of Eurosystem, such as:

- Define and implement the monetary policy of the Euro area.
- Promote the smooth operation of payment systems. Thus, contribute to the integration and stability of the Euro area Money Market.

The system is designed to process domestic and cross-border payments denominated in Euro. The aim is to allow large value payments (those related to Foreign Exchange (FX) and Money Market (MM) transactions are made throughout the Euro area at low cost with high security and short processing times). The payments are handled individually as it is a Real Time Gross Settlement (RTGS) system.

Unconditional payment orders are automatically processed one at a time on a continuous basis. Thus, TARGET2 provides immediate and final settlement of all payments (provided there are sufficient funds or overdraft facilities available on the payer’s account with its central bank). There is no minimum amount set for a payment made using TARGET2. In TARGET2, the payment services in Euro are available across a geographical area (which is larger than the Euro area). National central banks that have not adopted the Euro can also participate in TARGET2 to help the settlement of transactions. TARGET2 becomes mandatory, when:

- New member states join the Euro area
- Settlement of any Euro operations involves the Eurosystem

It uses SWIFT as the network for exchanging messages between participant banks and settlement system. It is based on SWIFT Net FIN Y-copy service.

[Types of Payment and Messages](#)

TPH supports generation and processing of the following:

- Customer transfer
- Bank to bank transfer
- Cover payments

Additionally, it generates SWIFT MT messages (that are compliant to TARGET2 specification) for outward payments. However, TARGET2 validates inward payments for compliance when received in TPH. TPH supports the following TARGET2 message types:

| Message | Description | TPH Support |
| --- | --- | --- |
| MT103 | Customer credit transfer | Inward and outward |
| MT103+ | Single customer credit transfer STP | Inward and outward |
| MT202 | General financial institution transfer | Inward and outward |
| MT202COV | General financial institution transfer (Inward only) | Inward only |
| MT019 | Abort notification | Inward only |

The below diagram depicts the flow of messages between TPH bank and TARGET2. TPH bank acts as a direct participant and the green boxes are Temenos systems.



- Payment can be initiated in one of the following methods:

- Manually from an ordering bank (account holding institution)
- Received as instruction from client as pain.001 file
- Input by back office user from Order Entry (OE) page

- TPH bank (as originator) processes the request and generates an MT103, MT103+ or MT202 towards TARGET2.
- TARGET2 clearing sends the SWIFT acknowledgement to TPH bank. If TARGET2 cannot settle the payment, it sends MT019 that is processed by TPH.
- TPH bank (as beneficiary) receives MT103, 202 or 202COV as a beneficiary bank.

[Payment Instruments](#)

TARGET2 is an RTGS system that supports credit transfers only.

[Bank Identifier Code (BIC)](#)

The preferred bank or branch identification method used in TARGET2 is BIC (BIC is mandatory to address the TARGET2 sender and receiver in SWIFT header). TPH supports BIC based payment capture and processing.

[Message Priority](#)

TARGET2 allows to set two priorities for payments:

- Normal
- Urgent

Urgent priority payments are delivered to the receiver participant on urgent priority over normal priority payments. It does not impact the order or settlement, and are settled in the order received. TARGET2 payments are processed as normal payments by default (which can be configured).

[Reachability](#)

Reachability of the beneficiary bank for all outward TARGET2 payments is validated against TARGET2 directory. The beneficiary bank is reachable, when the:

- BIC of the beneficiary participant is available in the directory for TARGET2 service.
- Closure date of the record is null or greater than the payment execution date.
- Status of the record is not N.

[Cut-Off Time](#)

TARGET2 has separate cut-off times for customer and bank to bank payments (which can be configured in TPH).

- 17.00 for customer payments
- 18:00 for bank transfers

[Cover Payments](#)

TARGET2 supports cover payments. Participants can send cover payments in the form of MT202COV referring to the underlying payment (MT103 or 103+) or to beneficiary bank using non-TARGET2 route (SWIFT). TPH supports receiving cover payments from TARGET2. It also performs cover matching with underlying payment (if configured), until which the Cover payment is held in a queue.

- If a match is found, the cover and underlying payment is further processed. It raises the following accounting entries:

- Payment processing - DR cover suspense account, CR beneficiary account
- Cover processing - DR TARGET2 Nostro account, CR cover suspense account

- If a match is not found, TPH raises a warning, forward entries and parks it in a queue until the payment.

The user can manually release the cover, which then proceeds with accounting postings.

[RMA Check as a Direct Participant](#)

All payments sent to TARGET2 needs to have Relationship Management Application (RMA) check (as TARGET2 use SWIFT Net FIN services). This check is performed for the given message type and receiving participant. TPH allows to set the following:

- Configure SWIFT message types for which RMA is not required. During payment processing, these message types are exempted from RMA check.
- Configure a set of message types for a given correspondent bank (TARGET2 receiver). During payment processing, TPH validates whether relationship exists between the given TARGET2 receiver and message type.

- RMA settings can be uploaded (using file upload) automatically or captured manually.
- RMA check is not performed for non-payment messages.

[Outward Payment Processing](#)

This section describes the outward processing of an order initiated in TPH bank.



| Activity | Description |
| --- | --- |
| Manual Capture of TARGET2 payment from branch or back-office using Order Entry | User captures a TARGET2 payment from TPH Order Entry (OE) page. Validates the mandatory and non-mandatory fields on submission, and indicates an error (if any). |
| Payment instructions using ordering bank | Ordering party’s bank (same as TPH or another bank) sends payment instructions to TPH bank.   The instructions can be in SWIFT MT or any ISO20022 format. |
| Account validations | Validates whether the ordering account is a valid Temenos Transact account.  It has sufficient balance to cover the transaction and no posting restrictions. |
| Bank Code validations | Validates whether the beneficiary bank code is valid (by validating BIC against SWIFT BIC directory). Important: This is performed when the directory is loaded, and system is configured to validate the bank code.  If the user has not entered the beneficiary bank BIC, the system derives it based on IBAN (if available). |
| Business validations | Instructed amount needs to be empty. If provided, currency needs to be in EUR. |
| Reachability Check | Validates whether the beneficiary bank (BIC) is reachable directly (if configured). |
| Balance Check | The system checks whether the debit account has enough funds to process the payment. If available, it reverses the funds. |
| Submission and supervisor approval | Processes the payment as follows:  1. On submission, the payment awaits supervisor’s approval. 2. Once approved, it is moved for further processing. 3. If the supervisor rejects, the payment can be modified and resubmitted for approval. 4. Payment is then sent to Temenos Payments Hub Engine for further processing.   Payments received in TPH from external banks in STP mode do not wait for Supervisor’s approval. |
| Warehouse | Warehouses the payments with future execution date, and then released on the SOD of the execution date. |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is a bank specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| RMA check | Performs the check on receiving bank. |
| Routing | Routes the payment to TPH clearing channel (TGT). This is configured to route to TARGET2 using SWIFT network. Clearing channel in turn determines the message type (MT103 or 202). If clearing cut-off is in the past for TARGET2, the payment is routed using an alternate channel, or warehoused by TPH to release it on the next business day.  Routing using an alternate channel is available only with PH license. |
| Dates calculation | Calculates the payment value and booking dates, which are configured to current date (same as execution date) |
| FX calculation | Applies when customer and payment account currencies are different. If any FX shifts are involved, it adjusts the value date (accordingly forward) and warehouses the payment.   This feature is only supported with PH license. |
| Balance reservation | Reserves funds on the debit account. Balance reservation is done on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, then it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges. The charge mode can be BEN, SHA or OUR for TARGET2 payments. |
| Duplicate check | Performs the check on payments received from an ordering bank for the configured set of payment attributes, such as payment amount, currency and transaction reference.  To know more about the criteria, refer to Duplicate Check section. |
| Posting | Debits the payment amount and charges to be borne by the customer to the Debtor’s account. If posting fails due to insufficient funds, payment is parked in the Repair queue for user action (Automatic Retry, Reject or Cancel).  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode. - If AMS is external, then it generates posting request in a native XML format and accepts response from the external system.  Outward Payments Entries are made before sending MT103 or MT202 to TARGET2  - Debit debtor account - Credit TARGET2 Clearing Nostro account  Inward Payments Entries are made when an MT103 or MT202 is received from TARGET2.  - Debit TARGET2 Clearing Nostro account - Credit Customer account  Settlement Booking Entry When TARGET2 payments are processed, the clearing Nostro is directly credited or debited (as above).   A separate settlement processing is not available, hence, there is no settlement accounting for TARGET2 payments. |
| TARGET2 channel validations | Performs all TARGET2 specific validations on payment to ensure it meets the compliance requirements. |
| Outward payment generation | Generates MT103 or MT202, and parks the payment in ‘Awaiting acknowledgement’ status. TARGET2 payments can be found by the service-code value (TGT) available in *103* field of Block 3 SWIFT message. |
| Error queue | Displays an error when processing the TARGET2 payment. It moves the transaction to Error queue for the user to repair or cancel the payment. |

[Inward Payment Processing](#)

This section describes the inward processing of a payment that is received from TARGET2 (destined to an account in TPH bank).



| Activity | Description |
| --- | --- |
| TARGET2 payment received from SWIFT network | Receives inward payment (MT 103 or 202) from TARGET2 (using SWIFT network or SWIFT gateway) in TPH. |
| TARGET2 specific format validations | TPH performs TARGET2 specific validations on the payment. These validations are different from standard SWIFT validations on MT103 or 202. |
| Account Validation | Validates the beneficiary account.  - Beneficiary sort code or account number unknown - Beneficiary account closed - Beneficiary account stopped - Account is not in currency quoted |
| Bank Code validation | If the payment is destined for an indirect participant, the system validates creditor BIC. |
| Dates calculation | Receives TARGET2 payments with value date as current business date. The payment is processed immediately. |
| Filtering | Performs filtering of payments, (if configured). This is a bank specific requirement that is performed in the site. |
| Fee calculation | Only applicable for customer transfers. |
| Duplicate check | Performs the check on payments received from TARGET2 for the configured set of payment attributes, such as payment amount, currency, and transaction reference. |
| Credit posting | Debits the TARGET2 clearing Nostro account, and posts the credit to the beneficiary (59A) or account with institution (57A), when TPH bank is a direct participant. |
| Error queue | Displays an error when processing the TARGET2 payment. It moves the transaction to Error queue for the user to repair or cancel the payment. |

## Illustrating Model Parameters

To know more on parameter setup for Trans-European Automated Real-time Gross Settlement Express Transfer System (TARGET2) clearing, refer the [Temenos Payment (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

This module provides the facility to send and receive credit transfers from TARGET2 clearing.

In this topic

- [Introduction to TARGET2 Clearing](#IntroductiontoTARGET2Clearing)

- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [Temenos Payments Hub](../../Payments_Hub_(PP)/Misc/Introduction.htm)
- [Clearing Directory](../../Clearing_Directory_(CA)/Misc/Introduction.htm)
- [APIs](../../APIs/Misc/APIs.htm#EP)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:19:48 PM IST