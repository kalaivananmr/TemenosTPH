# Introduction to Jordan RTGS - Typesofparticipants

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Jordan/Jordan/Jordan_PPJDNC/Introduction.htm#TypesofParticipants

---

# Introduction to Jordan RTGS

Updated On 22 March 2025 |
 10 Min(s) read

Feedback
Summarize

Jordan Real-Time Gross Settlement (JO – RTGS) is a domestic funds transfer system that allows participants to send or receive single Fund Settlement Instructions (FSIs). FSIs are settled on a gross basis and in real time, based on sufficient funds or limit held by the participant.

JO − RTGS offers secure, reliable, and real-time method of payment that adheres to international standards. It handles Credit Transfers (CT) and also provides a settlement point for all netting systems in Jordan (which is operated through the central accounts of banks held by the Central Bank of Jordan). The rules and procedures for the operations of participants is governed by Central Bank of Jordan.

Membership is mandatory for all operating commercial banks in Jordan.

The accounts of member banks held at the Central Bank of Jordan are used as settlement accounts for the system. The balances in these accounts represent the legal Required Reserve (RR) along with additional amounts, which is partly used for daily transactions. The system supports Jordan Dinar and U.S. Dollar denominated payments now. However, other currencies can be added to the system in future. It can perform the following:

- Process domestic payments
- Allow large-value payments, such as Foreign Exchange (FX) and Money Market (MM) transactions (to be made at low cost with high security and short processing times).

RTGS uses SWIFT network as a primary messaging scheme between its members and the system, whereas it uses a closed secured network between banks (s an alternative one).

## Types of Participants

This section shows the participant of Jordan RTGS:

| Type of Participant | Description |
| --- | --- |
| Direct Member | A participant bank that exchanges payments directly to JO – RTGS and maintains a current account with Central Bank Jordan in the currency of the transaction |

## Types of Payment and Messages

TPH supports generation and processing of Customer Transfer and Interbank Transfer. It generates SWIFT MT messages that are compliant to JO – RTGS specification. Additionally, it validates the inward payments received for SWIFT compliance. TPH supports the following JO-RTGS message types:

| Message | Description | TPH Support |
| --- | --- | --- |
| MT103 | Customer credit transfer | Inward and outward |
| MT202 | General financial institution transfer | Inward and outward |

The below diagram shows the message flow between TPH bank and JO – RTGS, with TPH bank acting as a direct participant.

Boxes in green are Temenos systems.



1. Back-Office Operator of the bank can initiate payment from Order Entry (OE) page.
2. TPH (as Originator) processes the request and generates an MT103 or MT202 towards JO – RTGS.
3. TPH bank (as Beneficiary) receives MT103 or MT202.

## Payment Instruments

JO – RTGS is an RTGS system that supports Credit Transfers (CT) only.

## Bank Identifier Code (BIC)

This is the preferred bank or branch identification method used in JO – RTGS . This is mandatory to address the JO – RTGS Sender and Receiver (in SWIFT header). TPH supports BIC based payment capture and processing.

## Cut-Off Time

Cut-off time for customer or bank transfers in JO – RTGS is 16:00 hrs. It is configurable in TPH in PP.CHANNEL.CUTOFF table.

## Outward Payment Processing

This section describes the outward processing of an order initiated in TPH bank.



| Activity | Description |
| --- | --- |
| Manual capture of JO – RTGS payment from branch or back-office by using OE page | Captures a JO – RTGS payment from TPH OE page.   - Validates the mandatory and non-mandatory fields on submission and indicates an error (if any). |
| Account validations | Validates whether ordering account has the following:   - A valid Temenos Transact account - No posting restrictions - Sufficient balance to cover the transaction |
| Bank code validations | Validates the beneficiary bank code (BIC) against SWIFT BIC directory.  This is performed when the directory is loaded and the system is configured to validate the bank code. |
| Reachability check | Validates whether the beneficiary bank (BIC) is reachable directly (if configured in TPH). |
| Balance check or reservation | Checks whether the debit account has enough funds to process the payment. If available, it reverses the funds. |
| Submission and supervisor approval | The user needs to perform the following:   1. On submission, the payment waits for Supervisor’s approval. 2. Once approved, it is moved for further processing. 3. If the Supervisor rejects the payment, it can be modified and resubmitted for approval. 4. Payment is then sent to Temenos Payments Hub Engine for further processing. |
| Warehouse | Warehouses the payments with future execution date, and then released on the Start of Day (SOD) of the execution date. |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is a bank specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the payment to a TPH clearing channel (JO – RTGS) through SWIFT network. Clearing channel determines the message type (MT103 or MT202).  - If system finds that the clearing cut-off time for JO – RTGS has passed, it routes the payment through an alternate channel or TPH warehouses to release on the next business day (This is based on configuration). - Routing through an alternate channel is available only with PH license. |
| Dates calculation | Calculates the payment value and booking dates, which are configured to current date (same as execution date) |
| FX calculation | Applies when customer and payment account currency are different. If any FX shifts are involved, it adjusts the value date and warehouses the payment.  This feature is only supported with PH license. |
| Balance reservation | Reserves funds on the debit account. Balance reservation is done on payment amount with charges.   - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges for the payment.  Charge mode can be BEN, SHA or OUR for JO − RTGS payments. |
| Duplicate check | Performs the check on payment amount, currency and transaction reference for payments received from an ordering bank.  To know more on the criteria, refer to Duplicate Check section. |
| Posting | Debits the payment amount and charges to be borne by the customer to the debtor’s account. If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (such as automatic retry, reject or cancel).   - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.   **Outward Payments** − Entries made before sending MT103 or MT202 to JO − RTGS   - Debit debtor account - Credit JO − RTGS clearing nostro account. |
| Outward payment generation | Generates MT103 or MT202, and parks the payment in ‘Awaiting acknowledgement’ status.   - The service code value (JOD) can recognise JO − RTGS payments available in 103 field of Block 3 of the SWIFT message. |
| Error queue | If an error occurs during processing, it moves the transaction to Error queue for the user to repair or cancel the payment. |

## Inward Payment Processing

This section describes the inward processing of a payment received from Jordan RTGS, destined to an account in TPH bank.



| Activity | Description |
| --- | --- |
| JO − RTGS payment received from SWIFT network | An inward payment (MT103 or MT202) is received from JO −RTGS (through SWIFT network or gateway) in TPH. |
| SWIFT format validations | Performs basic SWIFT format validations on the payment. |
| Account validation | Validates the beneficiary account for the following:   - Beneficiary BIC or account number unknown - Beneficiary account closed - Beneficiary account blocked - Account is not in the quoted currency |
| Dates calculation | Receives JO − RTGS payments with value date as current business date and processes the payment immediately. |
| Filtering | Performs filtering of payments (if configured). This is a bank specific requirement and performed in the site. |
| Fee calculation | Applies only for customer transfers. |
| Duplicate check | Performs on payments received from JO − RTGS for the configured set of payment attributes, such as payment date, amount, currency, and transaction reference. |
| Credit posting | Debits JO − RTGS clearing Nostro account and posts credit to the beneficiary account (59A).  **Inward Payments** − Entries made when an MT103 or MT202 is received from JO − RTGS clearing.   - Debit JO − RTGS clearing nostro account - Credit customer account |
| Error queue | If an error occurs during processing, it moves the transaction to the Error queue for the user to repair or cancel the payment. |