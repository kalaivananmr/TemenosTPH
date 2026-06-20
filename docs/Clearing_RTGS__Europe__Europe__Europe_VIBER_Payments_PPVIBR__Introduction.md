# Introduction to VIBER Payments

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_VIBER_Payments_PPVIBR/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [VIBER Payments](../../Europe/Europe_VIBER_Payments_PPVIBR/Introduction.htm) > Introduction

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
  - [EPC SEPA Credit Transfer EPC SEPA Credit Transfer](../../Europe/EPC_SEPA_Credit_Transfer/Introduction.htm)
  - [EPC SEPA Direct Debit EPC SEPA Direct Debit](../../Europe/EPC_Direct_Debit/Introduction.htm)
  - [RPS German Cheque Processing RPS German Cheque Processing](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Introduction.htm)
  - [VIBER Payments VIBER Payments](../../Europe/Europe_VIBER_Payments_PPVIBR/Introduction.htm)
    - [Introduction](../../Europe/Europe_VIBER_Payments_PPVIBR/Introduction.htm)
    - [Configuration](../../Europe/Europe_VIBER_Payments_PPVIBR/Configuration.htm)
    - [Working with](../../Europe/Europe_VIBER_Payments_PPVIBR/Working_with.htm)
    - [Tasks](../../Europe/Europe_VIBER_Payments_PPVIBR/Tasks.htm)
    - [Outputs](../../Europe/Europe_VIBER_Payments_PPVIBR/Outputs.htm)
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

# Introduction to VIBER Payments

Updated On 22 March 2025 |
 15 Min(s) read

Feedback
Summarize

VIBER is a Real-Time Gross Settlement (RTGS) system, operated by the Magyar Nemzeti Bank (MNB). It is designed for high value and urgent single payments settlement in Hungarian Forint (HUF) currency. After automatic real-time settlement, the payments are final and irrevocable, and the affected participants are notified without delay. It also settles central bank, interbank and customer credit transfers. There is no transaction amount limit for VIBER payments. It uses the following:

- SWIFT network (SWIFT Y-copy service) for message exchanges between participant banks and settlement system.
- MT messages as a communication standard but remains within the Country (Outward).

## VIBER Participants

There are two type of participants in VIBER scheme:

| Type of Participant | Description |
| --- | --- |
| Direct Member | A participant bank that exchange payments directly to VIBER, and holds a settlement account in RTGS. |
| Indirect Member | A member bank that exchange payments with VIBER by using a VIBER direct member. An indirect member bank does not hold a settlement account in VIBER. |

## Types of Payment and Messages

TPH supports generation and processing of standard SWIFT MT messages that are compliant to VIBER specification for outward payments. Inward payments are validated for VIBER compliance when received in TPH. TPH supports the following types of VIBER messages:

| Message | Description | TPH Support |
| --- | --- | --- |
| MT103 | Customer credit transfer | Inward and outward |
| MT103 | Return message | Inward and outward |

The below diagram shows the message flow between TPH bank and VIBER, with TPH bank acting as a direct participant.



1. `Payment Order (PO)` application (within TPH bank) or ordering customer bank (account holding institution) initiates the payment manually.
2. TPH processes the request, generates an MT103 and sends it to VIBER clearing.
3. If the receiver bank cannot process the payment, it returns the MT103 (that is received). TPH then processes it at the sender bank (sender of the original transaction).

## Payment Instruments

VIBER is an RTGS system that supports Credit Transfers only.

## Bank Identifier Code (BIC)

This is a preferred bank or branch identification method used in VIBER. However, it mandatorily enables to address the VIBER sender and receiver in SWIFT header.

## Message Priority

Message priority is set as ‘15’ in tag 113 in the outgoing MT103 for all payments generated by TPH.

## Reachability

The GVT clearing directory for VIBER is automatically uploaded in TPH, when received from Clearing Operator GIRO. It performs reachability based on G-Code and payment channel of the sending or receiving bank. The G-Code of the sending and the receiving bank is derived from the IBAN or BBAN of the debtor and creditor, respectively.

To know more, refer to [Clearing Directory Upload](../../Clearing_Directory_(CA)/Misc/Introduction.htm#Clearing_Directory_Upload) and [Reachability Check](../../Clearing_Directory_(CA)/Misc/Introduction.htm#Reachability_Check) section.

VIBER performs the following:

- Validates only outward credit transfer payments for reachability
- Does not validate the outward returns and inward credit transfer payments
- Parks the payment that fails reachability check in the Repair queue

## Cut-Off Time

Different cut-off times for customer transfer (MT103) can be configured in TPH. Default time setting is 23:59 for all payment types.

## Indirect Participation in VIBER

TPH can be configured to initiate or receive payments as an indirect participant bank (interacting with VIBER) using a VIBER direct participant. These participants are registered in GVT directory as an indirect participants (identified with a direct VIBER participant). Payment request can be sent to direct participant by using standard VIBER or proprietary format (which is developed as part of the project implementation). It allows to apply the standard inward and outward processing flows with an exception to disable some of the functionalities (for example, skip reachability check).

## Relationship Management Application (RMA) Check as a Direct Participant

This check is performed on all the payments that are sent to VIBER (as VIBER uses SWIFTNet FIN service), given message type, and receiving participant. TPH allows to configure the following:

- SWIFT message types for which RMA is not required.
- Set of message types for a given correspondent bank (VIBER receiver). TPH validates whethera relationship exists between VIBER receiver and message type during payment processing.

- RMA settings can be automatically uploaded through file upload or captured manually.
- RMA check is not performed for non-payment messages.

## Outward Payment Processing

This section describes the outward processing of an order initiated in TPH or ordering bank (as an indirect participant bank).



| Activity | Description |
| --- | --- |
| Manual capture of VIBER payment from branch or back-office using `PO` application or Order Entry (OE) page | Captures a VIBER payment from `PO` application or TPH OE page. Validates mandatory and non-mandatory fields on submission, and displays an error (if any). |
| Payment instructions through ordering bank | Ordering bank (same as TPH or another bank) sends payment instructions in SWIFT MT format to the TPH bank. |
| Account validations | Validates whether the ordering account is a valid Temenos Transact account with no posting restrictions and has sufficient balance to cover the transaction. |
| Bank code validations | Validates whether the beneficiary bank code by validating the BIC (mandatory user input field) against SWIFT BIC directory (if the directory is loaded, and system is configured to validate the bank code).  - Additionally, system validates if beneficiary BIC is provided. If provided, then the country at position 5, 6 is GB. |
| Business validations | Instructed amount needs to be empty. If it is provided, the currency as HUF (if provided). The transaction currency needs to be equal to HUF. |
| Reachability check | Validates whether the beneficiary bank is reachable directly or indirectly (if configured) in TPH or `PO` application by using the sort code derived from IBAN or BBAN. |
| Balance check | Checks whether the debit account has enough funds to process the payment. If available, the funds are reserved. |
| Warehouse | Warehouses the payments with future execution date and releases it on the SOD of the execution date. |
| Filtering | Performs filtering of payments when interfaced to a screening application. This is a bank specific requirement and has to be undertaken during implementation. TPH solution is pre-integrated with Temenos FCM solution for screening. |
| RMA check | Performs the check on the receiving bank. |
| Routing | Routes the payment to a TPH clearing channel (HUF), which is configured to send it to VIBER (through SWIFT network. Clearing channel in turn determines the message type (MT103). If the system finds that the clearing cut-off time for VIBER has passed, it routes the payment through an alternate channel (if configured) or TPH warehouses (timed warehouse) to release on the next business day. Routing through an alternate channel is available only with a ‘PH’ license. |
| Dates calculation | Calculates the payment value and booking dates, which is configured to the current date (same as execution date). |
| Balance reservation | Reserves funds on the debit account. This is performed on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges. Charge mode is always set as Shared (SHA) for VIBER payments. |
| Duplicate check | Performs the check on payments received from ordering or indirect participant bank for the configured set of payment attributes, such as payment amount, currency and transaction reference. |
| Posting | Debits the payment amount and charges to be borne by the customer to the Debtor’s account. If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (Automatic Retry, Reject or Cancel).  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode. - If AMS is external, it generates posting request in a native XML format and accepts response from the external system.   Outward Payments − Entries made before sending MT103 to VIBER   - Debit debtor (or ordering bank account) - Credit VIBER clearing Nostro account   Inward Payments − Entries made when an MT103 is received from VIBER   - Debit VIBER clearing Nostro account (or direct participants account when TPH bank is an indirect participant) - Credit customer account |
| VIBER channel validations | Ensures the payment meets the compliance requirements of VIBER. |
| Outward payment generation | Generates MT103 and parks the payment in ’Awaiting Acknowledgement’ status. VIBER payments can be recognised by the service-code value (HUF) available in Field 103 of Block 3 of the SWIFT message. |
| Error queue | If an error occurs, when processing a VIBER payment, it moves the transaction to Error queue for the user to repair or cancel the payment. |

## Inward Payment Processing

This section describes the inward processing of a payment received from VIBER and archived to an account in TPH bank or another bank (indirect participant).



| Activity | Description |
| --- | --- |
| VIBER payment received from SWIFT network | Receives an inward payment (MT103) from VIBER (through SWIFT Network or gateway) in TPH. |
| VIBER specific format validations | Performs VIBER specific validations on the payment in addition to the standard SWIFT validations on MT103. |
| Account validation | Validates the beneficiary account for the following:  - Unknown account number - Closed or not active - Account is not in HUF currency |
| Bank code validation | Validates the creditor BIC to verify if the payment is destined for an indirect participant. |
| Dates calculation | Processes the VIBER payments received with value date as current business date (immediately). |
| Filtering | Performs filtering of payments (if configured). This is a bank specific requirement and is performed during implementation. |
| Fee calculation | Only applicable for customer transfers (Charge bearer is always SHA). |
| Duplicate check | Performs duplicate check on payments received from VIBER for the configured set of payment attributes, such as payment amount, currency and transaction reference. |
| Credit posting | VIBER clearing Nostro account is debited, and credit is posted to the beneficiary account (59A) or account with institution (57A) when TPH bank is a direct participant of VIBER. |
| Payment archived, or redirected to indirect participant | If TPH bank is a correspondent bank, it redirects the payment to the account with institution bank (indirect participant). The redirected payment can be in SWIFT or proprietary formats agreed between TPH bank and Indirect participant bank (format is implemented locally by implementation team). Payment redirection is part of Agency banking functionality, and is available only with PH license. |
| Error queue | If an error occurs when processing a payment, it moves the transaction to the Repair queue for the user to repair or cancel the payment. |

## Auto-Return of Inward Payments

This section describes the auto-return processing of a payment received from VIBER, which failed business validations.



The system needs to be configured for automated returns with respect to VIBER clearing messages. If an inward VIBER payment is not validated successfully (as a result of applied business validations), and functional errors (such as account closed, credit freeze, invalid account, duplicate message) are raised, the beneficiary account cannot be credited. Hence, the funds of the incoming payment are credited to the customer account and the system creates a new VIBER return payment. This debits the customer account and credits the VIBER Clearing Nostro account. VIBER return payment is always sent as a MT103 message to VIBER clearing.

| Activity | Description |
| --- | --- |
| Posting − inward VIBER payment | Debits the VIBER clearing Nostro account and posts the credit to the customer account. |
| Create new return payment | Creates a new return payment for the inward VIBER payment (automatically), which is not successfully validated. |
| Posting − return payment | Debits the customer account and posts credit to the VIBER clearing Nostro account. |

## Manual Return of Inward Payments

The user can manually return the inward VIBER payments from the Repair queue. The system should not be configured for automated returns. This routes the invalid payment to the repair queue for the user to return the payment. Manual return processing is similar to auto-return functionality. To know more, refer to [Auto Return of Inward VIBER Payments](#Auto-Return_of_Inward_VIBER_Payments) section.



## Inward Return Payment Processing

This section describes the inward processing of a return payment received from VIBER.



| Activity | Description |
| --- | --- |
| VIBER return payment received from SWIFT Network | Receives an inward return payment (MT103) from VIBER (through SWIFT Network or gateway) in TPH. System identifies an inward MT103 payment from VIBER clearing as a return payment based onthe existence of code word RETN in tag 72 of the message. |
| VIBER specific format validations | Performs VIBER specific validations on the payment. |
| Identify original payment | Identifies the original outgoing payment transaction (being returned) by using the transaction reference number available as part of code word MREF in the *72* field of the MT103 (return payment) message. |
| Account determination | Determines the account to be credited in response to the inward return payment based on the original debtor’s account from the original outgoing payment transaction (being returned) |
| Dates calculation | Processes the VIBER payments received with value date as current business date (immediately). Sends the future dated payments to warehouse. |
| Filtering | Performs filtering of payments (if configured). This is a bank specific requirement and is perfomed during implementation. |
| Duplicate check | Performs duplicate check on payments received from VIBER for the configured set of payment attributes, such as payment amount, currency and transaction reference. |
| Credit posting | Debits the VIBER clearing Nostro account and posts the credit to the original debtor’s account (from where the original outgoing payment transaction is returned). |
| Original payment marked as ‘Returned’ | If the return payment is successfully posted, the system changes the status of the original payment that is returned from ‘Completed’ to ‘Returned’. |

## Illustrating Model Parameters

To know more on parameter setup for VIBER CT, Returns and Refusals, refer the [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Suite (PH)](../../Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm) user guides.

## Illustrating Model Products

This module provides the facility to send and receive domestic transfers through VIBER.

In this topic

- [Introduction to VIBER Payments](#IntroductiontoVIBERPayments)

- [VIBER Participants](#VIBERParticipants)
- [Types of Payment and Messages](#TypesofPaymentandMessages)
- [Payment Instruments](#PaymentInstruments)
- [Bank Identifier Code (BIC)](#BankIdentifierCodeBIC)
- [Message Priority](#MessagePriority)
- [Reachability](#Reachability)
- [Cut-Off Time](#CutOffTime)
- [Indirect Participation in VIBER](#IndirectParticipationinVIBER)
- [Relationship Management Application (RMA) Check as a Direct Participant](#RelationshipManagementApplicationRMACheckasaDirectParticipant)
- [Outward Payment Processing](#OutwardPaymentProcessing)
- [Inward Payment Processing](#InwardPaymentProcessing)
- [Auto-Return of Inward Payments](#AutoReturnofInwardPayments)
- [Manual Return of Inward Payments](#ManualReturnofInwardPayments)
- [Inward Return Payment Processing](#InwardReturnPaymentProcessing)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [APIs](../../APIs/Misc/APIs.htm#EP)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:20:14 PM IST