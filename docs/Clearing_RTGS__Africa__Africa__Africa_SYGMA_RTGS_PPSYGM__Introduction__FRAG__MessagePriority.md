# Introduction to SYGMA RTGS - Messagepriority

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm#MessagePriority

---

# Introduction to SYGMA RTGS

Updated On 22 March 2025 |
 11 Min(s) read

Feedback
Summarize

Système des gros montants automatisé (SYGMA) is a Real-Time Gross Settlement (RTGS) platform within the payment and financial framework of the central bank of Central African States, Banque des Etats de L’Afrique Centrale (BEAC) that offers same-day CFA Franc (XAF) fund transfers.

SYGMA is operational in all CEMAC countries since 19 November, 2007. It performs liquidity transfers in central currency (individually and irrevocably), and finalised when the provision in the settlement account is available and sufficient.

Additionally, it performs the following:

- Supports customer and bank transfers.
- Enables movement of funds from ordering customer to the beneficiary that belongs to another bank, on the same day.
- Uses BEAC clearing system as the network for message exchanges between a participant bank and settlement system. It uses the SWIFT Y-Copy service.

## SYGMA RTGS Participants

Direct member is a participant bank that exchanges payments directly with SYGMA and holds an account with SYGMA for settlement. BEAC provides each participant with an XML file containing the list of all participants in the system, including Central Bank participants. Each national entity of the Central Bank is a direct participant in SYGMA. This file also has all central bank branches.

- BIC (or BIC pseudo) code
- Settlement account number

## Types of Payment and Messages

SYGMA supports the following message types:

| Message | Description |
| --- | --- |
| MT103 | Payment order on behalf of an individual client |
| MT202 | Order for a financial institution |
| MT900 | Confirmation of debit |
| MT910 | Confirmation of credit |
| MT199/999 | Free message |

The message flow between TPH bank and SYGMA RTGS, with TPH bank acting as a direct participant is shown below.



1. Payment initiation can happen through the below sources:
   - User initiates from PAYMENT ORDER (PO) application  Standing Order
   - Ordering customer/bank can send MT101 and TPH processes it to SYGMA as MT103
   - Bulk payment or Online Tax  Payments (OTP) is uploaded and forwarded to SYGMA as MT103
2. TPH processes the payment, debits the ordering customer, and sends an MT103 or MT202 to SYGMA as SWIFT (Y-COPY).
3. On receipt of the payment, SYGMA performs the following:
   - Settles the payment
   - Forwards it to the receiving participant bank
   - Sends the settlement confirmation to both sending and receiving banks (TPH does not handle settlement confirmation)
4. At the receiving bank, TPH accepts the payment and performs validation and credit posting.
5. Temenos Transact receives and stores MT910 (Confirmation of Credit) and manually matches it with customer or bank transfer and proceeds with settlement.
6. If the payment needs to be returned, it is moved to the Manual queue for user action (to cancel, reverse or resend the payment).

## Bank Identifier Code (BIC)

The preferred beneficiary’s bank or branch identification method used in SYGMA is BIC. BIC is used (mandatory)  to address the SYGMA Sender and Receiver (in SWIFT header).

However, SYGMA also supports Relevé d'identité bancaire (RIB) to address the beneficiary account. It is a pre-printed form with the bank account number and sort codes for national transactions.

RIB code is used for bulk payments to control the validity of the beneficiary RIB. It is the concatenation of:

- Bank code (5 characters)
- Branch code (5 characters)
- Account number of beneficiary (11 characters)
- Control digits (2 characters)

Temenos Transact uses the algorithm provided by the BEAC to calculate the control digit based on the bank code, branch code, and account number of beneficiary.

## Message Priority

SYGMA clearing prioritises the payments based on the following:

- Normal
- Urgent

## Outward Payment Processing

This section describes the outward processing of an order initiated in TPH bank.



| Activity | Description |
| --- | --- |
| Manual capture of SYGMA payment from branch or back-office by using PO application or Order Entry (OE) page | Captures a SYGMA payment from PO application or TPH Order Entry (OE) page.  - Any error encountered during validations of fields (mandatory and non-mandatory) are displayed on the page To know more on SYGMA manual capture, refer to SYGMA Manual Capture section. |
| Payment instructions through ordering bank | Sends payment instructions to TPH bank The instruction can be in SWIFT MT or any ISO20022 format. |
| Account validations | Validates whether ordering account has no posting restrictions and has sufficient balance for the transaction |
| Bank code validations | Performs the following validations:  - RIB code or BIC against SWIFT BIC directory (if the directory is loaded, and system is configured to validate the bank code). - Beneficiary BIC or RIB is available. If beneficiary BIC is available, the country at position 5, 6 is CM. |
| Business validations | Ensure the instructed amount is empty. If a value is provided, the currency needs to be a local currency (XAF) of the CEMAC region The transaction currency needs to be equal to the local currency. |
| Reachability check | Validates whether the beneficiary bank (BIC) is reachable directly (if configured in TPH or PO application) |
| Balance check (not shown in diagram) | Checks whether the debit account has enough funds to process the payment. If available, the funds are reserved. |
| Submission and supervisor approval | The user needs to perform the following:  1. On submission of the payment, it waits for Supervisor’s approval. 2. Once approved, payment is moved for further processing.    - If the Supervisor rejects the payment, it is modified and resubmitted for approval. 3. Payment is then sent to TPH for further processing. Payments received from external banks in STP mode do not wait for Supervisor’s approval. |
| Warehouse | Warehouses the payments with future execution date. These payments are then released on the SOD of the execution date |
| Filtering | Performs filtering of payments when interfaced to a screening engine. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution |
| Routing | Routes the payment to TPH clearing channel (SYG) through SWIFT network. Clearing channel determines the message type (MT103 or MT202) If system finds that the clearing cut-off is in past for SYGMA, TPH warehouses the payment for releasing it on the next business day. |
| Dates calculation | Calculates the payment value date and booking date, which are configured to current date (same as execution date) |
| Balance reservation | Reserves funds on the debit account. Balance reservation is done on payment amount with charges  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system |
| Fee calculation | Calculates the applicable charges for the payment Charge mode is set as Shared (SHA) for SYGMA payments. |
| Duplicate check | Performs the check on payment amount, currency and transaction reference received from an ordering bank To know more, refer to Duplicate Check section. |
| Posting | Debits the payment amount and charges to be borne by the customer to the debtor’s account (according to fee calculation). If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (such as automatic retry, reject or cancel).  - If Account Management System (AMS) is Temenos Transact, then TPH performs debit posting in embedded mode - If the AMS is external, it generates posting request in XML format and accepts response from the external system   **Outward Payments** – Entries made before sending MT103 or MT202 to SYGMA.   - Debit Customer Account (or ordering bank account for 202) - Credit SYGMA Clearing Nostro Account   **Inward Payments** – Entries made when an MT103 or MT202 is received from SYGMA.   - Debit SYGMA Clearing Nostro Account - Credit Customer Account   **Settlement Booking Entry** – Processing the SYGMA payments credits or debits the clearing Nostro directly. There is no separate settlement processing and hence no settlement accounting for SYGMA payments. |
| SYGMA channel validations | Performs all SYGMA specific validations on the payment to ensure it meets the compliance requirements of SYGMA. It performs the following validations:   - Duplicate check - RIB validation - Name conformity check |
| Outward payment generation | Generates MT103 or MT202 message, and parks the payment in ‘Awaiting Acknowledgement’ status  - The service-code value (SYG) can recognise SYGMA payments available in Field 103 of Block 3 of the SWIFT message |
| Error queue | If an error occurs during processing, it moves the payment to Repair queue |

## Inward Payment Processing

This section describes the inward processing of a payment received from SYGMA, destined to an account in TPH bank.



| Activity | Description |
| --- | --- |
| SYGMA payment received from SWIFT network | An inward payment (MT103 or MT202) is received from SYGMA (through SWIFT network or gateway) in TPH |
| SYGMA specific format validations | Performs the following SYGMA specific validations on the payment:  - Duplicate check - RIB validation - Name conformity check |
| Account validation | Validates the beneficiary account for the following:  - Beneficiary RIB or account number unknown - Beneficiary account closed - Beneficiary account stopped - Account is not in currency quoted |
| Bank code validation | It is not applicable, as the SYGMA RTGS does not support the Indirect Participant functionality in TPH |
| Dates calculation | Receives SYGMA payments with value date as current business date and processes the payment immediately |
| Filtering | Performs filtering of payments (if configured). This is a bank specific requirement and is performed in the site |
| Fee calculation | Applies only for customer transfers The charge bearer is SHA. |
| Duplicate check | Performs on payments received from SYGMA for the configured set of payment attributes, such as payment amount, currency, and transaction reference |
| Credit posting | Debits SYGMA clearing Nostro account and posts credit to the beneficiary account (59) or account with institution (57A) |
| Error queue | If any error occurs during processing, it moves the payment to repair queue |