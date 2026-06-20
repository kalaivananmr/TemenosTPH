# Introduction to Lebanon RTGS - Typesofpaymentandmessages

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Lebanon/Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm#TypesofPaymentandMessages

---

# Introduction to Lebanon RTGS

Updated On 22 March 2025 |
 10 Min(s) read

Feedback
Summarize

RTGS system in Lebanon is known as Banque Du Liban (BDL-RTGS), a Real Time Gross Settlement. It is a domestic funds transfer system where participants can send or receive single fund settlement instructions (FSIs). These FSIs are settled on a gross and real-time manner when participants have sufficient funds or credit facilities. The BDL-RTGS offers secure, reliable, and real-time method of payment that adheres to international standards. It governs the rules and procedures for the operations of participants. If it fails to abide by rules and procedures, it is subjected to applicable sanctions (as defined in the Code of Money and Credit and BDL regulations). Participation of financial institutions in the BDL-RTGS is not mandatory. The participant needs to maintain a current account in the books of BDL for each applicable currency, in which bank wants to send the transactions.

The system is designed to process domestic payments smoothly. Additionally, it aims to allow large value payments (such as those relating to Foreign Exchange (FX) and Money Market (MM) transactions) to be made at low cost with high security and short processing time. Payments are handled individually in an RTGS system. Once the payment order is submitted, it is automatically processed one at a time on a continuous basis. Thus, Lebanon RTGS provides immediate and final settlement of all payments, when sufficient funds or overdraft facilities are available in the payer’s current account with its central bank (BDL).

Minimum amount is not set for a payment made through Lebanon RTGS.

The primary connection to the BDL-RTGS is through Swift Message Carrier Network and is based on SWIFTNet FIN Y-copy service. Each participant needs to have a SWIFT Business Identification Code (BIC8) as a unique identifier that is connected to the Settlement Account in the BDL-RTGS.

## Types of Participants

Direct Member is a participant bank that exchanges payments directly to BDL-RTGS and maintains a current account with BDL-RTGS in the currency of the transaction.

## Types of Payment and Messages

Temenos Payments Hub (TPH) supports generation and processing of customer and interbank transfers. TPH performs the following:

- Generates SWIFT MT messages that is compliant to BDL RTGS specification for outward payments
- Validates inward payments for SWIFT compliance when received

TPH supports the following Lebanon RTGS message types:

| Message | Description | TPH support |
| --- | --- | --- |
| MT103 | Customer credit transfer | Inward and outward |
| MT202 | General financial institution transfer | Inward and outward |

The below diagram displays the flow of messages between TPH bank (acting as a direct participant) and Lebanon RTGS.

Boxes in green are Temenos systems.



- The banks back office operator can initiate a payment from the Order Entry (OE) page.
- TPH (as originator) processes the request and generates an MT103 or MT202 towards BDL-RTGS (Lebanon RTGS).
- TPH (as beneficiary bank) receives MT103 or MT202.

## Payment Instruments

Lebanon RTGS is an RTGS system that supports credit transfers only.

## Bank Identifier Code (BIC)

The preferred bank or branch identification method used in BDL-RTGS (Lebanon RTGS) is BICs. It is mandatorily equipped to address the BDL-RTGS (Lebanon RTGS) sender and receiver (in SWIFT header). TPH supports BIC-based payment capture and processing.

## Cut-Off Time

Cut-off time for customer or bank transfers in BDL-RTGS is 16:00 hours. It is configured in the CHANNEL CUT-OFF table of TPH.

## Outward Payment Processing

This section describes the outward processing of an order initiated in the TPH bank.



| Activity | Description |
| --- | --- |
| Manual capture of Lebanon RTGS payment from branch or back office using OE Page | - Captures a Lebanon RTGS payment from OE page of TPH. - Validates mandatory and non-mandatory fields on submission, and displays errors (if any). |
| Account validations | Validates whether the Ordering Account is a valid Temenos Transact account.  It has the following to cover the transaction:  - No posting restrictions - Sufficient balance |
| Bank code validations | Validates the BIC against SWIFT BIC directory (if configured). |
| Reachability check | Validates whether the beneficiary bank (BIC) is reachable directly (if configured). |
| Balance check or reservation | Checks whether the debit account has funds to process the payment. If available, the funds are reserved. |
| Submission and supervisor approval | Performs the following validations:  - On submission, the payment awaits for the Supervisor’s approval.   - If approved, it is moved for further processing.   - If rejected, it can be modified and resubmitted for approval. - Payment is then sent to Temenos Payments Hub Engine for further processing. |
| Warehouse | Warehouses the payments with future execution date and releases on the SOD of the execution date. |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is a bank-specific requirement and performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the payment to a TPH clearing channel (Lebanon RTGS) by using SWIFT network. Clearing channel in turn determines the message type (MT103 or 202). If the system finds that the clearing cut-off has past for Lebanon RTGS, it routes the payment through an alternate channel or warehouses (by TPH) to release it on the next business day. This feature is available only with Payments Hub (PH) license. |
| Dates calculation | Calculates the payment value and booking dates, which are configured to current date (similar to execution date). |
| FX calculation | Applies when customer and payment account currencies are different. If any FX shifts are involved, it adjusts the value date and warehouses the payment. This feature is only supported with PH license. |
| Balance reservation | Reserves funds on the debit account, which is performed on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges. The charge mode can be BEN, SHA or OUR for Lebanon RTGS payments. |
| Duplicate check | Duplicate check can be configured to happen based on payment amount, currency, and transaction reference for payments received from an ordering bank.  To know more, refer to Duplicate Check section. |
| Posting | Debits the payment amount and any charges to be borne by the customer to the debtor’s account. If posting fails due to insufficient funds, payment is parked in the Repair queue for user action (such as Automatic Retry, Reject or Cancel).  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.   Outward payments are made before sending MT103 or MT202 to Lebanon RTGS   - Debit debtor account - Credit Lebanon RTGS clearing Nostro account |
| Outward payment generation | Generates messages (MT103 or MT202) and parks the payment in ‘Awaiting acknowledgement’ status. Lebanon RTGS payments can be found by the service-code value (LBP) available in the *103* field of Block 3 SWIFT message. |
| Error queue | If an errors occurs while processing the Lebanon RTGS payment, it moves the transaction to the Error queue for the user to repair or cancel the payment. |

## Inward Payment Processing

This section describes the inward processing of a payment received from Lebanon RTGS, destined to an account in TPH bank.



| Activity | Description |
| --- | --- |
| Lebanon RTGS payment received from SWIFT network | Receives an inward payment (MT103 or 202) from Lebanon RTGS using SWIFT network or gateway. |
| SWIFT format validations | Performs basic SWIFT format validations on the payment. |
| Account validation | Validates the beneficiary account for the following:  - BIC or unknown account number - Closed or blocked - Not in currency quoted |
| Dates calculation | Receives Lebanon RTGS payments with value date as current business date. Payment is processed immediately. |
| Filtering | Performs filtering of payments (if configured). This is a bank-specific requirement and is performed at the site. |
| Fee calculation | Only applicable for customer transfers. |
| Duplicate check | Performs duplicate check on payments received from Lebanon RTGS for the configured set of payment attributes. The criteria is set to payment date, amount, currency and transaction reference. |
| Credit posting | Debits the Lebanon RTGS clearing Nostro account, and posts the credit to the beneficiary account (59A). Inward payments is made when an MT103 or MT202 is received from BDL-RTGS (Lebanon RTGS) clearing.  - Debit Lebanon RTGS clearing nostro account - Credit customer account |
| Error queue | If an error occur while processing Lebanon RTGS payment, it moves the transaction to the Error queue for the user to repair or cancel the payment. |

## Illustrating Model Parameters

To know more on on parameter setup for Lebanon RTGS, refer to [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

Lebanese RTGS module can send and receive the real time gross settlement payments in Lebanon.