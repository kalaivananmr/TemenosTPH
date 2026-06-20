# Introduction to BECS – Direct Entry Payments

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Australia/Australia/Australia_BECS_PPBECS/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Australia > BECS

- Australia;)
  - [BPAYBPAY](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm)
  - [BECSBECS](../../Australia/Australia_BECS_PPBECS/Introduction.htm)
    - [Introduction](../../Australia/Australia_BECS_PPBECS/Introduction.htm)
    - [Configuration](../../Australia/Australia_BECS_PPBECS/Configuring.htm)
    - [Working with](../../Australia/Australia_BECS_PPBECS/Working_with.htm)
    - [Tasks](../../Australia/Australia_BECS_PPBECS/Tasks.htm)
    - [Outputs](../../Australia/Australia_BECS_PPBECS/Outputs.htm)
  - NPP Payments;)
  - BPAY Agency Banking;)
  - AURTGS Clearing;)
  - DE (BECS) Agency Banking;)
  - Clearing Directory Upload and Reachability Check;)

Payments

# Introduction to BECS – Direct Entry Payments

Updated On 12 February 2026 |
 25 Min(s) read

Feedback
Summarize

Direct Entry (DE) is an electronic payment system in Australia that allows batch processing of payments. It provides an option to perform the following between bank accounts in Australia:

- Send payments to beneficiaries (Credit Transfers)
- Collect payments from payers (Direct Debits)

DE is used to setup the following:

- Monthly direct debits to pay insurance premium and other utility bills
- Salary and welfare payments
- Transfer of funds between bank accounts

The Bulk Electronic Clearing System (BECS, which is also known as CS2) is used to clear and settle a DE payment. All financial institutions participating in BECS are assigned an unique Bank State Branch (BSB) number. Participants of BECS can exchange the DE files (other than government files) in bulk, six times a day. Settlement occurs on the same-day after each of the first five official exchanges. The settlement for the last exchange happens on the next business day.

## DE Participants

Financial institutions participate in DE scheme as follows (depending on how they clear and settle with BECS):

|  |  |
| --- | --- |
| Tier 1 members or Direct Participants | Use an Exchange Settlement Account (which they maintain with BECS) to clear and settle directly. |
| Tier 2 members or Indirect Participants | Appoint a representative (Direct Participant) to clear and settle on their behalf. |

- Temenos Payments Hub Hub (TPH) can be configured to act as DE direct or indirect participant.
- The Direct participant gateway connectivity is not supported in the current product version.

## Payment Instruments

DE supports credit transfers and direct debits. TPH supports processing of the following:

- Outward credit transfer
- Inward credit transfer
- Inward direct debit payments

## Bank State Branch (BSB) Number

This is used to identify the individual branch of a financial institution. It consists of a six digit numerical code separated by a hyphen.

AAB-CCC

- First two numbers (AA) specify the financial institution.

- Third number (B) indicates the state where the branch is located.
- Last three numbers (CCC) are unique identifier for a branch.

## BECS Clearing Directory and Reachability Check

BECS provides a BSB clearing directory file on a monthly basis, which has the BSB number and other details of all participating banks. A full upload file and a Delta file is provided. The reachability of beneficiary bank (using BECS) for all outward DE payments can be validated against the BECS BSB clearing directory. The beneficiary bank is reachable, when:

- BSB number of the beneficiary bank is available in the directory
- Status of the record is ‘Active’
- Start Date of the record is not in future

TPH supports the following for BSB directory:

- Full file upload (is performed only during the initial system set up). .
- Delta file upload (Any further updates to BSB directory) must be handled by performing Delta file upload)

Reachability check can be configured in TPH based on the bank’s requirement. If configured, TPH can perform it during payment capture or processing.

## Returns and Refusal of Returns

|  |  |
| --- | --- |
| Returns | Banks can perform the following:  - Reject the received credit transfer or direct debit request - Send payment returns   All outward returns need to be sent within D+1 business days to BECS, where D is the date on which the inward credit transfer or direct debit is received from BECS. |
| Refusal of Returns | If the banks are unable to process the received payment returns, they can reject and send ‘Refusal of Returns’. All outward refusal of returns need to be sent within D+1 business days to BECS, where D is the date on which the inward return is received from BECS. |

## Types of Payments and Messages

DE scheme uses flat file format (EBCDIC) for electronic exchange of files between direct participants and BECS. Each file is made up of the following records:

| Record | Record Type |
| --- | --- |
| Descriptive or Header Record | 0 (common for all file types) |
| Detail Record | 1, 2 or 3 |
| File Total or Trailer Record | 7 (common for all file types) |

TPH supports the following types of BECS Direct Entry message:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| Type 1 | B2B | Customer credit transfer or Direct Debit The record type indicator for all the detail records has the value ‘1’. | - Credit Transfer − Inward and Outward - Direct Debit − Inward |
| Type 2 | B2B | Return The record type indicator for all the detail records has the value ‘2’. | - Credit Transfer Return − Inward and Outward - Direct Debit Return − Outward |
| Type 3 | B2B | Refusal of Return The record type indicator for all the detail records has the value ‘3’. | - Credit Transfer Refusal of Return − Inward and Outward - Direct Debit Refusal of Return − Inward |
| Combined Type 2 and Type 3 File | B2B | Return and Refusal of Return The record type indicator for all the detail records can have the value ‘2’ or ‘3’. | - Credit Transfer Return and Refusal of Return − Inward and Outward - Direct Debit Return and Refusal of Return − Inward |

The above message types are used for all exchanges between TPH and direct participant, and needs to adhere to the following rules in TPH:

- Inward Type 1 file from BECS clearing has separate bulks for Direct Debits and Credit Transfer.
- Inward Returns and Refusal of Returns can be received in the same file. CT Return/CT Refusal of Return can come in the same bulk. Similarly, DD Return/DD Refusal of Return can come in the same bulk. However, CT and DD Return/Refusal of Returns cannot come in the same bulk.

## Message Flow Diagram

BECS DE message flow is shown in the below image.



- Credit transfer payment initiation happens through the following sources:
  - Bank user can initiate payment request by using the PAYMENT.ORDER (PO) application.
  - Payment request are received through various customer channels (not supported in existing TPH version)
- TPH module performs the following:

- Sending bank (direct or indirect participant) – Processes the credit transfer payment request, debits the ordering customer and sends the Type 1 file to BECS at scheduled intervals, through either direct participant or BECS.

  TPH does not support Outward DD processing, hence, it is not depicted in the flow diagram.
- Receiving bank (direct or indirect participant) – Receives the Type 1 file from BECS through direct participant. The incoming Type 1 file has both Credit Transfer and DD request. It validates and processes the received payment request and then credits or debits the customer’s account for Credit Transfer or Direct Debit, respectively.

- All the incoming Credit Transfer or DD rejected by TPH are sent to BECS (or through Direct Participant) in a Type 2 Return file.
- The sending bank receives the Type 2 return file from BECS or through the direct participant. TPH module at the sending bank can accept the returned transactions and perform the required accounting reversals against the customer account.
- TPH module can also reject the returned transactions. All the ‘Refusal of return’ transactions are sent back to BECS in Type 3 file.

  It allows to send Returns or Refusal of Return transactions in the same outward file.

- The receiving bank gets the Type 3 file from BECS or through the Direct Participant. TPH module at the receiving bank processes the Refusal of Return transactions and performs the required accounting reversals.

## Initiating Customer Credit Transfers (CT)

DE Credit Transfer can be initiated in TPH by using the Payment Order (PO) screen. Currently, it does not support file upload of payment initiation request.

1. The user performs the following:
   - Enters the details, such as ordering and beneficiary customer, and the payment amount and currency.
   - Validates the payment order and commits the record.

     The beneficiary bank reachability check (if configured) is performed in the PO page by using the BECS Directory (maintained in TPH).
2. After the Authoriser’s approval, the system processes the payment order as a book or an outward payment depending on where the beneficiary resides. It generates Type 1 message for outward payments and sends it to clearing.

## BECS DE Cut-Off Time

DE payments can be sent to the BECS clearing, maximum of six times on a business day. The last submission window is at 10.30 pm (Sydney).

## Transaction Stop Request

DE scheme does not maintain mandates for processing Direct Debit (DD) payment. The bank need not accept the mandate before the executing DD instruction and sending it to the payer bank. However, debtor can setup a ‘Stop Direct Debit’ instruction to reject DD request received from a Billing Organisation, after a specified ‘Stop Date’.

## Outward Payment Processing

This section describes the processing of a Credit Transfer request initiated by PO application in a TPH bank.



| Activity | Description |
| --- | --- |
| Manual Capture of DE Credit Transfer Payment from branch or back-office using PO screen | User captures a DE Credit Transfer payment request from PO page. To know more, refer to [Manual Initiation of Direct Entry Payments](Working_with.htm#Manual_Capture). Validates the mandatory fields on submission and displays an error (if any). |
| Debit Account validations | PO application validates whether the ordering account is a valid and active Temenos Transact account, which has no posting restrictions. |
| Reachability Check | PO application validates whether the beneficiary bank (BSB code) is reachable by using DE payment scheme. |
| Submission and Supervisor approval | Performs the following actions:  - On submission of the payment, it waits for Supervisor’s approval. - Once approved, it is sent to TPH for further processing.   If the Supervisor rejects the payment, it is modified and resubmitted for approval. |
| Warehouse | Warehouses the payments with future execution date and releases on the SOD of the execution date. |
| Balance Check | Validates whether the debtor account has funds and then proceeds to reserve the required funds for processing the payment request. Balance reservation can be done on payment amount with or without charges (if any).  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Routing | Routes the payment to a BECS Direct Participant bank, based on the Routing configurations setup in TPH. |
| DE Cut-Off Check | Checks whether it exceeds the DE clearing cut-off. If exceeded, the payment is configured to move the processing date to the next business date and warehouse it (with PH license) or Repair queue. |
| Dates Calculation | Calculates the payment Value Date and Booking Date. |
| DE Channel validations | Performs the following validations (mandatory) on the payments to ensure it meets the compliance requirements of DE:  - Debtor Account - Payment Amount - Lodgement Reference (needs to have maximum length of 18 characters) - Creditor Account (needs to have a maximum length of 9 characters) |
| Duplicate Check | Enables to configure checks based on payment amount, currency and transaction reference of the payment transaction at the payment product level. Functional duplicate check is not configured in TPH for DE payments. |
| Filtering | Performs filtering of payments when interfaced to a screening engine.  This is a bank specific requirement that is performed in the site. |
| Charge Calculation | Calculates the applicable charges, according to the configured charge products. |
| Debit Posting | Debits the payment amount and charges to be borne by the customer to the Debtor’s account. Transaction posting entries are as follows:  - DR Debtor Account - CR Suspense Account  The following settlement entries are passed when the file is generated and sent to clearing:  - DR Suspense Account - CR Direct Participant Nostro Account |
| Bulking and Outward Payment File Generation | Bulks the transactions according to the bulking logic defined for clearing. The Transaction status is set as ‘Waiting Clearing’. Generates the outgoing Type 1 file, according to clearing frequency configuration. The Transaction status is set as ‘Completed’. |
| Repair | If an error occurs while processing a payment, it moves the transaction to Repair queue for the user to repair and resubmit or cancel the payment (with a reason description). If the validation fails, the processing flow is re-executed from Account Validation. The cancelled payment moves to ‘Cancelled’ status. |

## Inward Payment Return Processing

This section describes the processing of an Incoming Payment Return request in TPH bank, received from BECS or through direct participant.



| Activity | Description |
| --- | --- |
| Message Acceptance | Receives the return file and performs file level validation on the return message.  - If the validation failures, it rejects the full file. - If the validation is successful, it debulks the file and creates the return transactions. |
| Match with Original Payment | Matches the return with an original outward payment request, based on the following:  - Lodgement Reference - TPH Customer Account - Amount  If a matching payment is not found, the return transactions is sent to Repair queue where it can be manually ‘Refused’. To know more, refer to the [Outward Refusal of Return flow](#Outward_processing_%E2%80%93_Refusal_of_Return). |
| Acceptance Date Validation | Validates whether the return is received within 1 business day (configurable) after processing the original payment. Returns that are delayed cannot be resubmitted from the Repair queue, as it triggers an error. It can be returned, when it is within the configured acceptance days for Refusals of Returns. |
| Posting | Credits the payer account for returns according to the below posting:  - DR Suspense Account - CR Customer Account  Processes the settlement transaction entries passed after return file:  - DR Direct Participant Nostro Account - CR Suspense Account |
| Mark Original Payment as Returned | Updates the Original Payment status to ‘Payment Completed with Return’. |
| Repair | If an error occurs during payment processing, it moves the return transaction to Error queue (based on configuration) for the user to repair or return the payment (refused). The user can refuse the payment when it is performed within the acceptance days configured in TPH for outgoing refusal of returns. Auto rejection of return payment is not configured in TPH (with PH License), that isbecause ‘Refusal of Return’ has specific error codes that the user needs to select manually from the Repair page. All rejected Returns would result in creating ‘Refusal of Return’ message and sending it to BECS. |

## Outward Refusal of Return Processing

This section describes the processing of an Outward Refusal of Return request in TPH bank for a rejected inward return request.



| Activity | Description |
| --- | --- |
| Refusal of Return Initiation | Initiates after the refusal of an inward payment return that failed processing. |
| Routing | Routes the refusal of return payment to BECS clearing channel according to the routing configuration setup in TPH. |
| DE Cut-Off Time Check | Verifies whether the DE cut-off time is not crossed.  - If crossed, it triggers a routing error and does not send the payment.   The payment can be sent only on the next working day within the cut-off time |
| Posting | Posts the following entries against the original return transaction:  - DR Suspense Account - CR Refusal of Returns Suspense Account  Posts the following entries against the refusal of return transaction:  - DR Refusal of Returns Suspense Account - CR Suspense Account |
| Mark Return Payment as returned | Marks the original return transaction as ‘Returned’. The original outgoing credit transfer transaction remains in ‘Completed’ status. |
| Bulking and Outward Payment File Generation | Bulks the Refusal of Return Transactions according to the bulking rules. Creates and sends the outgoing Refusal (Type 3) transaction file according to the Clearing Frequency timing. Marks the transaction status as ‘Completed’. |
| Repair | Triggers an error in the Repair page during routing, such as cut-off or return acceptance days breach. |

## Inward Direct Debit Processing

This section describes the processing of an Incoming Direct Debit request in TPH bank received from BECS or through direct participant.



| Activity | Description |
| --- | --- |
| Message Acceptance | - Receives inward payment Type 1 file from direct participant - Performs file level validation on the received message   - If the validation fails, it rejects the file. - If the validation is successful, it creates a DD transaction. |
| Account Validation | Validates the debtor account and checks for the following:  - Account number is valid - Account is active - Account does not have posting restrictions |
| Debit Authority | Validates whether ‘Stop Instruction’ is setup against the debtor account in the Transaction Stop module. If the ‘Stop Instructions’ are available and matches the ‘BECS User ID’ and ‘Lodgement Reference’ of the received DD request, then TPH performs the following:  - Validates whether the request is received within the ‘Stop Payment Date’. - If not, the payment is sent to Repair queue. |
| Balance Check | Validates whether the debtor account has enough funds and can proceed to reserve the required funds for processing the direct debit request. If the Balance Check fails, it parks the payment in Repair queue with the appropriate error description. |
| Dates Calculation | If the DE payments are received with value date as current business date, it processes the payment immediately. |
| Duplicate Check | Enables to configure checks based on payment amount, currency, and transaction reference of the payment transaction. Functional duplicate check is not configured in TPH for DE payments. |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is a bank specific requirement that is performed in the site. |
| Fee Calculation | Debits fee associated with payment from the customer account, based on the fee product configured in TPH. |
| Account Posting | Raises the following accounting entries for the received DD:  - DR Customer Account - CR Suspense Account  Processes the following inward files in settlement entry:  - DR Suspense Account  - CR Direct Participant Nostro Account |
| Repair | If an error occurs while processing an inward direct debits, it routes the transaction to the Repair queue or returned automatically. If routed to repair, the user can repair the direct debit from the Repair page or returns the direct debit (manually) from the Repair queue (with an appropriate return code). The following can be performed in TPH:  - The user returns the transaction when performed within the acceptance days. - Auto rejection of payments are available. - Creates and sends all returns that results in return payment (Type 2). |

## Inward Credit Transfer Processing

This section describes the processing of an incoming credit transfer request in TPH bank received from BECS or through direct participant.



| Activity | Description |
| --- | --- |
| Message Acceptance | Preforms the following in TPH:  - Receives inward payment Type 1 file from direct participant. - Does file level validation on the received message.   - If the validation fails, it rejects the file gets rejected. - If the validation is successful, it creates a credit transfer transaction. |
| Account Validation | Validates the credit account for the following:  - Account Number is invalid - Account is active - Account does not have posting restrictions |
| Dates Calculation | If DE payments receives Value Date as Current Business Date, the payment is processed immediately. |
| Duplicate Check | Enables to configure checks based on payment amount, currency, and transaction reference of the payment transaction. Functional duplicate check is not configured in TPH for DE payments. |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is a bank specific requirement and is performed in the site. |
| Fee Calculation | Debits the fee associated with payment from the customer account, based on the fee product configured in TPH. |
| Account Posting | Raises the following accounting entries for the received credit transfers:  - DR Suspense Account - CR Customer Account  Processes the following files in settlement entry:  - DR Direct Participant Nostro Account - CR Suspense Account |
| Repair | If an error occurs while processing an inward credit transfers, it routes the transaction to Repair queue or returned automatically. If it routes to repair, the user can repair the transaction from the Repair page or returns it manually from the Repair queue (with an appropriate return code). The following can be performed in TPH:  - The user can return the transaction when it is performed within the acceptance days. - Auto rejection of payments are available. - Creates and sends all returns that result in return payment to BECS (as a Type 2 file). |

## Outward Return Payment Processing

This section describes the processing of an Outward Payment Return request in TPH, for a rejected inward credit transfer or direct debit request.



| Activity | Description |
| --- | --- |
| Return Initiation | Initiates outward return payment after the return of an inward CT or DD payment that failed processing. |
| Routing | Routes return payment to BECS clearing channel, according to the routing configuration setup in TPH. |
| DE Cut-Off Time Check | Verifies that the DE cut-off time is not crossed. If crossed, it warehouses and sends the return on the next business date (that is, automated returns with PH license). If manual return is involved, it triggers the error on the page for cut-off or return acceptance day breach. |
| Posting | **Outward Return against Inward CT Transactions**  The following entries are posted against the original CT transaction:  - DR Suspense Account - CR Returns Suspense Account  The following entries are posted against the return transaction:  - DR Returns Suspense Account - CR Clearing Suspense Account  **Outward Return against Inward DD transactions** The following entries are posted against the original DD transaction:  - DR Returns Suspense Account - CR Suspense Account  The following entries are posted against the return transaction:  - DR Suspense Account - CR Return Suspense Account |
| Mark return Payment as refused | Marks the original return transaction as ‘Completed with Return’. |
| Bulking and Outward Payment File Generation | Bulks the return transactions according to the bulking rules. Creates and sends outgoing Return (Type 2) transactions file according to the Clearing Frequency timing. Marks the transaction status as ‘Completed’. |
| Repair | Triggers an error in the Repair page during routing, such as cut-off or return acceptance day breach. |

## Inward Refusal of Return Processing

This section describes the processing of an Incoming Refusal of Return request in TPH bank, received from BECS or through direct participant.



| Activity | Description |
| --- | --- |
| Message Acceptance | Performs file level validation on the received file.  - If the validation fails, it rejects the entire file. |
| Match with Original Return | Matches the Refusal of Return transaction with an original outward payment return transaction. This is performed based on the following:  - Lodgement Reference - TPH Customer Account - Amount   If a matching return payment is not found, it sends the ‘Refusal of return’ transaction to Repair queue. |
| Posting | The Refusal of Return received for the CT Return is sent to the following:  - DR Suspense Account - CR Unposted Items Suspense Account  The Refusal of Return received for the DD Return is sent to the following:  - DR Unposted Items Suspense Account - CR Suspense Account |
| Repair | If an error occurs during payment processing, it moves the transaction to Error queue for the user to repair payment and park the funds in the Unposted Suspense account. This is configured to not allow the return of a ‘Refusal of Return’ transaction. |

## Outward File Generation

BECS is a secured and automated clearing for Australia. Temenos Payments Hub now supports the direct debit collection processing of BECS clearing.

This functionality allows banks to manage direct debits for BECS clearing.

## Illustrating Model Parameters

To know more on parameter setup for BECS CT, DD, Returns and Refusals, refer to [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

PPBECS module provides the facility to send and receive domestic CT and DD transfers via Bulk Electronic Clearing System (BECS).

In this topic

- [Introduction to BECS – Direct Entry Payments](#IntroductiontoBECSDirectEntryPayments)
  - [DE Participants](#DEParticipants)
  - [Payment Instruments](#PaymentInstruments)
  - [Bank State Branch (BSB) Number](#BankStateBranchBSBNumber)
  - [BECS Clearing Directory and Reachability Check](#BECSClearingDirectoryandReachabilityCheck)
  - [Returns and Refusal of Returns](#ReturnsandRefusalofReturns)
  - [Types of Payments and Messages](#TypesofPaymentsandMessages)
  - [Message Flow Diagram](#MessageFlowDiagram)
  - [Initiating Customer Credit Transfers (CT)](#InitiatingCustomerCreditTransfersCT)
  - [BECS DE Cut-Off Time](#BECSDECutOffTime)
  - [Transaction Stop Request](#TransactionStopRequest)
  - [Outward Payment Processing](#OutwardPaymentProcessing)
  - [Inward Payment Return Processing](#InwardPaymentReturnProcessing)
  - [Outward Refusal of Return Processing](#OutwardRefusalofReturnProcessing)
  - [Inward Direct Debit Processing](#InwardDirectDebitProcessing)
  - [Inward Credit Transfer Processing](#InwardCreditTransferProcessing)
  - [Outward Return Payment Processing](#OutwardReturnPaymentProcessing)
  - [Inward Refusal of Return Processing](#InwardRefusalofReturnProcessing)
  - [Outward File Generation](#OutwardFileGeneration)
  - [Illustrating Model Parameters](#IllustratingModelParameters)
  - [Illustrating Model Products](#IllustratingModelProducts)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Wednesday, June 17, 2026 2:21:53 PM IST