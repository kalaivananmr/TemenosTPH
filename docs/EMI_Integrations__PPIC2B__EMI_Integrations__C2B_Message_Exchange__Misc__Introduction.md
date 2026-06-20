# Introduction to C2B Message Exchange

> Source: https://docs.temenos.com/docs/Solutions/Payments/EMI_Integrations/PPIC2B/EMI_Integrations/C2B_Message_Exchange/Misc/Introduction.htm

---

2. [Payments](../../../../../content/payments.html)
3. You are here:
   C2B Message Exchange > Introduction

- C2B Message Exchange;)
  - [Introduction](../../../EMI_Integrations/C2B_Message_Exchange/Misc/Introduction.htm)
  - [Configuration](../../../EMI_Integrations/C2B_Message_Exchange/Misc/Configuration.htm)
  - [Working with](../../../EMI_Integrations/C2B_Message_Exchange/Misc/Working_with.htm)
  - [Tasks](../../../EMI_Integrations/C2B_Message_Exchange/Misc/Tasks.htm)
  - [Outputs](../../../EMI_Integrations/C2B_Message_Exchange/Misc/Outputs.htm)

Payments

# Introduction to C2B Message Exchange

Updated On 22 March 2025 |
 42 Min(s) read

Feedback
Summarize

'C2B Message Exchange' solution in Temenos Payments Hub supports EMI (Electronic Money Institution) to send payment initiation requests to their payment bank (typically a big bank with clearing connectivity) based on ISO 20022 messages in the customer to bank (C2B) space. The 'C2B Message Exchange' solution can also be used by small banks which interact with another bank through C2B messages for executing payment transactions. This module is dependent on Temenos Payments Hub ACH framework module.

Context diagram of the EMI (implemented in Temenos Payments Hub) is shown below.



'Payment Bank' and 'Clearing' shown in above diagram are only for understanding the solution. The payment bank executes the payment transactions using the EMI account held with it and sends credit transfers or direct debits to the beneficiary or debtor respectively. The scope of the 'C2B Message Exchange' solution is limited to the EMI implemented in Temenos Payments Hub.

## Supported Message Formats

Temenos Payments Hub supports the following ISO message formats:

| Message | Description | Direction |
| --- | --- | --- |
| pain.001.001.09 | Credit Transfer (CT) Initiation | Outward |
| pain.008.001.08 | Direct Debit (DD) Initiation | Outward |
| pain.002.001.10 | Status Report for CT/DD Initiation | Inward |
| camt.054.001.10 | Debit Credit Notification | Inward |

Refer to [Supported attributes](#202501) section to know more details on attributes considered by Temenos Payments Hub.

## Initiating Credit Transfer Requests

Temenos Payments Hub supports the following modes for credit transfer initiation.

| Mode | Description |
| --- | --- |
| Electronic Banking Channels | Temenos Payments Hub can receive credit transfer initiation requests through the Payment Order API for payment initiation. |
| Branch | Branch users can initiate credit transfer requests using the Payment Order application and Order Entry screen. |
| T24 Business Applications | Temenos Payments Hub can receive credit transfer requests from T24 business applications through the Payment Order application. |
| Feeder Channels | Temenos Payments Hub can receive and process pain.001. The system supports both single and bulk pain.001 transactions. |

For all the above modes, Temenos Payments Hub replaces the debtor (EMI Customer) and debtor account details with that of the EMI and EMI account during message generation. The EMI customer and account details are populated by the system in the ultimate debtor fields. Refer outward payment generation in [Outward Processing of Credit Transfer Initiation Request to Payment Bank](#OutwardProcessing) section to know more details on the outward pain.001 message

The system ignores any details on ultimate debtor if provided at time of initiation from above modes and does not map in the outward pain.001 sent to payment bank. This is because the system automatically maps the EMI customer and account details in the *Ultimate Debtor* field of outward pain.001. Also, any details on intermediary agent or account if provided is not mapped in the outward pain.001 since the EMI is typically expected to have a bilateral relationship with payment bank.

## Outward Processing of Credit Transfer Initiation Request to Payment Bank

This section describes the outward processing of a credit transfer initiation request initiated in Temenos Payments Hub through the Payment Order application or Order Entry screen or pain.001 message. Temenos Payments Hub bulks the credit transfer initiation requests using the [Bulking Criteria](#Bulking) and sends the outward pain.001 file to Payment Bank.



The table below shows the activities involved in Outward Processing of Credit Transfer Initiation Request to Payment Bank.

| Activity | Description |
| --- | --- |
| Manual capture of credit transfer request from branch or back office by using Payment Order (PO) application or Order Entry (OE) page | Captures a credit transfer request from PO application or Temenos Payments Hub OE page. Validates mandatory and non-mandatory fields on submission and displays error (if any). |
| Payment initiation using pain.001 message | EMI customer initiates a credit transfer request by sending a pain.001 message |
| Account validations | Validates the following for the ordering account:   - Is a   valid Temenos Transact account. - Has no posting   restrictions. - Has sufficient balance   to cover the transaction. |
| Reachability check | Skipped since the EMI is typically expected to have a bilateral relationship with the Payment Bank |
| Balance check (not shown in diagram) | Checks whether the debit account has enough funds for the payment to be processed. If available, it reserves the funds. |
| Submission and Supervisor approval | For payments received from PO application or OE screen, Temenos Payments Hub performs the following validation:   - On submission of   payment, it waits for Supervisor’s approval.   - Once approved, it is     moved for further processing.   - If rejected, it is     modified and resubmitted for approval. - It is then sent to   Temenos Payments Hub Engine for further processing. - Payments received in   STP mode (inward pain.001 file) do not wait for Supervisor’s approval. |
| Warehouse | Warehouses payments with future execution date and releases on the SOD of the execution date. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement, which is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes the payment to a Temenos Payments Hub clearing channel (ISOC2B), which is configured to route to payment bank. Clearing channel determines the message type (pain.001). |
| Dates calculation | Calculates the payment value and booking dates, which is configured to current date (similar to the execution date) |
| FX calculation | Applies when customer account and payment account currencies are different. If FX shifts are involved, it adjusts value date forward and warehouses the payment. This feature is supported with Payments Hub (PH) license. |
| Balance reservation | Reserves funds on the debit account. It is done on payment amount with charges.   - If Account Management   System (AMS) is Temenos Transact, then Temenos Payments Hub performs   funds reservation in embedded mode. - If the AMS is   external, it generates fund reservation request in a standard XML format   and accepts response from the external system. |
| Fee calculation | Calculates the applicable charges.  Since the ISO pain.001 message format has provision to only indicate the charge bearer, any charges computed by the system are not mapped in the outward pain.001 and any mechanism to handle charges between EMI and payment bank is out of scope of this solution. |
| Duplicate check | Performs duplicate check on payments received for a set of payment attributes, such as payment amount, currency and transaction reference. |
| Posting | Debits the payment amount and any charges to be borne by the customer to the debtor account. If posting fails due to insufficient funds, it parks the payment in the Repair queue for user action (automatic retry, reject or cancel).   - If Account Management   System (AMS) is Temenos Transact, then Temenos Payments Hub performs   debit posting in embedded mode. - If the AMS is   external, it generates posting request in a native XML format and   accepts response from the external system.   The following entries are made for outward credit transfer requests before sending pain.001 to payment bank.   - Individual transaction   entries   - Debit debtor account     (or ordering bank account)   - Credit suspense     account - Settlement transaction   entries (bulk)   - Debit suspense     account   - Credit Nostro account. |
| Channel validations | Banks can add additional rules specific to processing required by the payment bank. The system performs basic checks conforming to ISO 20022 xsd schema validations for pain.001.001.09 message. |
| Outward payment generation | Generates pain.001.001.09 message with the below key characteristics   - Debtor Details: The   system populates the   details of the EMI as the debtor. Name, Address related field are   mapped from the values configured in COMPANY. Identification related   field (BIC) of the EMI is mapped from PP.COMPANY.PROPERTIES - Debtor Account Details: Clearing account   number configured in PP.CLEARING.SETTING is mapped as the debtor account   number of the EMI. - Debtor Agent Details: Debtor BIC/NCC which   is configured in PP.CLEARING as the clearingBic or   clearingNcc/clearingSystemIdCode - Ultimate Debtor Details: EMI customer details   are mapped under Ultimate Debtor. IBAN or account number of the EMI   customer are mapped under Organisation Id> Other Id attribute - Requested Execution Date: The credit value date   determined in Temenos Payments Hub is mapped as the requested execution   date - Address Details: As per ISO schema,   both structured and unstructured address details are permitted and no   specific rules are defined for formation of structured address. Since   the address related details may vary with region, the system populates both   unstructured and structured address fields - Instruction Identification: 'FT Number' of the   transaction is mapped as the instruction identification - End to End Identification: In case the detail is   not available, the system map the value as 'NOTPROVIDED' |
| Error queue | If an error occurs while processing the payment, it moves the transaction to the Error queue for the user to repair or cancel the payment. |

## Initiating Direct Debit Collection Requests

Temenos Payments Hub supports the following modes for direct debit initiation.

| Mode | Description |
| --- | --- |
| Branch | Branch user can initiate direct debit initiation requests using the Order Entry screen |
| Feeder Channel | Temenos Payments Hub can receive and process pain.008. The system supports both single and bulk pain.008 transactions. |

For all the above modes, Temenos Payments Hub replaces the creditor and creditor account details as that of the EMI and EMI account during message generation. The EMI customer and account details are populated by the system in the ultimate creditor fields. The charge option supported for direct debit initiation requests is 'SHA'. Any other charge option received in the initiation request is converted to 'SHA' by the system during outward processing. For more details on the outward pain.008 message, please see outward payment generation in outward processing section.

The system ignores any details on ultimate creditor if provided at time of initiation from above modes and does not map in the outward pain.008 sent to payment bank. This is because the system automatically maps the EMI customer and account details in the Ultimate Creditor fields of outward pain.001.

## Outward Processing of Direct Debit Initiation Request to Payment Bank

This section describes the outward processing of a direct debit initiation request which is initiated in Temenos Payments Hub through Order Entry screen or pain.008 message. Temenos Payments Hub bulks the direct debit initiation requests using the bulking criteria and sends the outward pain.008 file to Payment Bank.



The table below shows the activities involved in Outward Processing of Direct Debit Initiation Request to Payment Bank.

| Activity | Description |
| --- | --- |
| Manual capture of DD initiation from branch or back office by using Order Entry (OE) page | - Captures a DD from Temenos Payments Hub OE page. - Validates (mandatory and non-mandatory) fields and inputs data on submission. |
| Payment initiation using pain.008 message | EMI customer sends DD payment initiation instructions to Temenos Payments Hub. The instruction is in the pain.008.001.02 or pain.008.001.08 – ISO20022 format. |
| File duplicate check | Checks whether a file is received from a channel other than OE. If a duplicate file is found, it rejects and sends a negative pain.002 message to the initiating bank or system (if configured). This check is based on the following combination of fields in the pain.008 file:   - Group header message identification - Message format of the file - Group header initiating party organisation ID, BIC - Source from which the pain.008 file is originated |
| Format validation | Validates the pain.008 message format by checking mandatory and non-mandatory fields, proper field length, and content based on XML schema. |
| Bulk agreement validation | - Validates pain.008 bulks against a netting agreement setup for the submitter of the bulk. - To perform this, go to **Admin Menu** > **Payment Hub** > **Debit Authority** > **Netting Agreements**.   - Netting agreement validation can be skipped when the MessageType (pain.008) is configured in the No DA List (in the Debit Authority menu). - Bulk agreement validation is not applied for DD initiated from Temenos Payments Hub OE page. |
| Credit account validation | Validates the following for the ordering account:   - Is a valid Temenos Transact Account - Does not have a posting restriction |
| Execution warehouse | Warehouses DD initiations that are received 14 calendar days (or more) prior to the RCLD (which is configured in *Max Allowed Days* in Source settings) or scheduled for release on RCLD minus 14 calendar days. The following is performed in a DD batch that is received 14 calendar days (or more) before RCLD:   - Warehouses the parent (total amount) transaction. - Creates child transactions from the batch when the parent transaction is released and validates it successfully. |
| Determine outgoing clearing | Routes the payment to a clearing channel (ISOC2B), which is configured to route to payment bank. |
| Reachability check | Skipped since the EMI is typically expected to have a bilateral relationship with the Payment Bank. |
| Channel validations | Banks can add additional rules specific to processing required by the payment bank. The system performs basic checks conforming to ISO 20022 xsd schema validations for pain.008.001.08 message. |
| Dates calculation | Calculates the DD (debit and credit) value dates and booking date. Basics rules for date calculation for outgoing transactions are as follows:   - If the RCLD of the DD initiation is equal to or before the current business date, the collection or settlement date is set one banking business date ahead from the current business date (based on the configured settlement shift for the respective clearing). - If the clearing cut-off time has already passed when applying the settlement shift, the system applies another cut-off shift day (1 day).   Calculates the debit and credit value dates and book date, which is equal to determined collection or settlement date. |
| Duplicate check | Enables to configures the check based on the following criteria:   - DD batch booking (parent transaction that books the total amount)   - Account of the Credit Party   - Currency of the Credit Account   - Transaction Amount   - Currency   - RCLD   - Bulk Reference - Each DD transaction in a batch   - Account of the Debit Party   - Currency of the Debit Account   - Transaction Amount   - Transaction Currency   - RCLD   - Instruction Identification - Single outgoing DD transaction (batch booking is false)   - Account of the Credit Party   - Currency of the Credit Account   - Transaction Amount   - Transaction Currency   - RCLD   - Instruction Identification   The system can configure and change (if required) the duplicate checks. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Outward Payment Generation | Bulks DD initiations and sends a pain.008 message to the payment bank, when:   - DD transactions are received at least 14 days prior the given RCLD. - All business validations are qualified.   Generates pain.008.001.08 message with the below key characteristics:   - Creditor Details The system populates the details of the EMI as the creditor. Name, Address related fields are mapped from the values configured in COMPANY. Identification related field (BIC) of the EMI is mapped from PP.COMPANY.PROPERTIES - Creditor Account Details Clearing account number configured in PP.CLEARING.SETTING is mapped as the creditor account number of the EMI. - Creditor Agent Details Creditor BIC/NCC which is configured in PP.CLEARING as the clearingBic or clearingNcc/clearingSystemIdCode - Ultimate Creditor Details EMI customer details are mapped under Ultimate Creditor. IBAN or account number of the EMI customer are mapped under Organisation Id> Other Id attribute - Requested Collection Date The debit value date determined in Temenos Payments Hub is mapped as the requested collection date - Address Details As per ISO schema, both structured and unstructured address details are permitted and no specific rules are defined for formation of structured address. Since the address related details may vary with region, the system populates both unstructured and structured address fields. - Instruction Identification 'FT Number' of the transaction is mapped as the instruction identification. - End to End Identification In case the detail is not available when payment is initiated from OE, the system maps the value as 'NOTPROVIDED'. |
| Warehouse future dated | Warehouses DD initiations or schedules for release on the calculated debit value date (which is equal to settlement or collection date). |
| Fees calculation | Charges creditor for any fees. Fees for child DD transactions are booked or posted (similar to single DD transactions and not along with batch parent transaction).  Since the pain.008 message format has provision to only indicate the charge bearer, any charges computed by the system does not be mapped in the outward pain.008 and mechanism to handle charges between EMI and payment bank is out of scope of this solution. |
| Posting | Credits the creditor’s account with the transaction amount. If the posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or is cancelled. To know more, refer to Error Queue section.  **Posting**   - If a DD initiation is a child of a batch (booking indicator is true or configured as a part of the netting agreement), then:   - Debit suspense account is configured in Clearing setting   - Credit batch suspense account is configured for each company - If a DD initiation is a single transaction (booking indicator is false or configured as a part of the netting agreement), then:   - Debit suspense account is configured in Clearing setting   - Credit creditor is the ordering client - Total requested bulk amount of a batch booking transaction is known as the parent transaction of the batch children, in which:   - Batch suspense account is configured for each company   - Credit creditor is the ordering client   **Settlement Booking Entry**   - The system creates and posts a separate settlement transaction to move funds between the Nostro and suspense account. |
| Error queue | If an error occurs while processing the direct debit request, it moves the transaction to the repair queue for user intervention or cancels the payment |

## Bulking Criteria

The system bulks the outward credit transfer initiation requests and direct debit initiation requests which are pending to be sent to payment bank using the below criteria:

- Transaction currency
- Message type (such as pain.001 or pain.008)
- Clearing transaction type (CT or DD)
- Credit value date in case of CT and Debit Value Date in case of DD

For every bulk that is formed, the system maps the batch booking indicator as 'True' during outward message generation.

## Channel Validations

Temenos Payments Hub performs only the validations which are necessary to ensure that generated credit transfer initiation request or direct debit initiation request meet the ISO xsd schema specifications of pain.001.001.09 and pain.008.001.08 respectively. Most of the existing core validations result in a message which is compliant with xsd schema. Additionally, as a channel validation, Temenos Payments Hub performs the below:

For outward credit transfer/direct debit initiation requests, if Debtor/Ultimate-Debtor/Creditor/Ultimate-Creditor private identification details are provided relating to date and place of birth, the user must provide all the below attributes.

- BirthDate
- CityOfBirth
- CountryOfBirth

## Handling Status Report for Credit Transfer Initiation and Direct Debit Initiation Request

Payment bank can provide the status of the file(pain.001) sent by the EMI with a pain.002 message. Temenos Payments Hub processes the acceptance and rejection response for the pain.001 based on the status code indicated in the pain.002.

| Scenario Description | File Level Status | Bulk Level Status | Transaction Level Status |
| --- | --- | --- | --- |
| File is fully accepted | ACSP | NA | NA |
| File is fully rejected | RJCT | NA | NA |
| File is partially accepted  (Bulks in the file could be fully rejected or partially accepted) | PART | RJCT | RJCT |
| PART | PART | RJCT |

Interpretation of the file/bulk/transaction level status done by the system for processing the response is as below:

| Level | Attribute (pain.002) |
| --- | --- |
| File Level Status | Document>OriginalGroupInformationAndStatus>GroupStatus |
| Bulk Level Status | Document>OriginalPaymentInformationAndStatus>PaymentInformationStatus |
| Transaction Level Status | Document>OriginalPaymentInformationAndStatus>TransactionInformationAndStatus>TransactionStatus |

Temenos Payments Hub processes the status report received from payment bank in STP mode. When the file is fully rejected, it is parked for manual action from the file level exception enquiry under payment exceptions. When the file is partially accepted, individual bulk could be either fully rejected or partially rejected. Temenos Payments Hub expects the transaction level details of the rejected transactions in the bulk to be available in the pain.002.

'C2B Message Exchange' solution does not support processing of technical positive acknowledgment(ACK) or negative acknowledgement(NACK).

## Matching to Original Transaction

Temenos Payments Hub expects the individual reference(s) of the original transaction(s) to be mandatorily provided in the pain.002 when a bulk is partially accepted and optionally if bulk is fully rejected for the outward pain.001/pain.008 message sent to Payment Bank. Pain.002 message has the below attributes for matching to the original pain.001/pain.008 at individual transaction level.

- Original Instruction Identification
- Original End To End Identification
- Original UETR

It is recommended that 'Original Instruction Identification' be provided by the Payment Bank for matching to original transaction.

Temenos Payments Hub can match to the original transaction based on 'Original Instruction Identification' as long as the underlying transaction(CT/DD) is not archived in Temenos Payments Hub. Transactions which are in status range '991' to '999' are eligible for archival. Refer [Introduction to Housekeeping Functions](../../../../../Payments/PP/Payments_Hub_(PP)/House_Keeping_Functions/Introduction.htm) user guide to know more about the archival process. If the underlying transaction gets archived, the transaction detail received in pain.002 is left unmatched and the overall file status of the pain.002 is 'Unmatched' even if one of the transactions included in the pain.002 could not be matched.

For the 'C2B Message Exchange' solution, Temenos Payments Hub can also match to the underlying transaction(CT/DD) based on 'Original End To End Identification' and 'Original UETR' for a period of 5 working days from the date the pain.001/pain.008 file is sent to the payment bank. Beyond five working days, the received transaction is 'Unmatched' similar to scenario described above for the match based on 'Original Instruction Identification'.

For payments initiated through order entry, the value 'NOTPROVIDED' if received in pain.002 for ' Original End To End Identification' will not be matched since it is included by the system only during outward message generation and is not stored internally.

## Receiving Debit Credit Notifications from Payment Bank

EMI can receive credit notification from the Payment Bank for any credit transfer received on the EMI account(held in Payment Bank). Similarly, a debit notification can be received for any direct debit transaction booked on the EMI account. Temenos Payments Hub supports receiving single debit or credit notification from Payment Bank through camt.054.001.10 message.

Temenos Payments Hub only considers the below attribute of camt.054 and processes the notification as a book transfer involving the clearing nostro account and account number configured in suspense account in PP.CLEARING.SETTING. All notifications received from Payment Bank based on source as 'ISOC2B' are booked by Temenos Payments Hub without application of any criteria.

| Attribute | Camt.054 Mapping |
| --- | --- |
| Transaction Amount | Document > Notification > Entry > Amount |
| Transaction Currency |

Posting Entries raised as part of the debit or credit notification processing are given below.

- Debit Advice: Credit Clearing Nostro Account, Debit Suspense Account
- Credit Advice - Debit Clearing Nostro Account, Credit Suspense Account

Any additional details on the payment which are received in the camt.054 are stored in local ref fields in Temenos Payments Hub.

## Supported Attributes

The Attributes of Pain.001.001.09 considered by Temenos Payments Hub is listed below.

| Attribute Name | Description | Mandatory/Optional |
| --- | --- | --- |
| Message Identification | Indicates the message identifier of the pain.001 file. | Mandatory |
| Creation Date Time | Indicates the creation date and time of the pain.001 file. | Mandatory |
| Number of Transactions | Indicates the total number of transactions included in the pain.001 file. | Mandatory |
| Control Sum | Indicates the total value of the transactions included in the pain.001 file. | Optional |
| Initiating Party Name | Indicates the name of the party requesting the payment initiation. This detail is of the EMI implemented in Temenos Payments Hub. | Optional |
| Initiating Party Address | Indicates the unstructured address lines of the party requesting the payment initiation. This detail is of the EMI implemented in Temenos Payments Hub. | Optional |
| Initiating Party BIC | Indicates the identifier of the party requesting the payment initiation. This detail is of the EMI implemented in Temenos Payments Hub. | Mandatory |
| Payment Information Identification | Indicates the unique identification of the bulk. | Mandatory |
| Payment Method | Indicates the method used to move money between debtor and creditor. Credit Transfer is the supported option. | Mandatory |
| Batch Booking | Indicates whether the debtor agent must book a single debit entry per bulk included in the pain.001 or multiple debit entries on the debtor account for transaction included in the bulk. | Optional |
| Number of Transactions per bulk | Indicates the number of transactions included in the bulk. | Optional |
| Control Sum per bulk | Indicates the total value of transactions included in the bulk. | Optional |
| Requested Execution Date | Indicates the date at which the debtor(EMI) requests the payment bank to process the payment. | Mandatory |
| Debtor Name | Indicates the name of the debtor. This is the name of EMI implemented in Temenos Payments Hub. | Optional |
| Debtor Address | Indicates the unstructured address lines of the debtor. This is the address information of EMI implemented in Temenos Payments Hub. | Optional |
| Debtor BIC | Indicates the identifier of the debtor. This is the BIC of the EMI implemented in Temenos Payments Hub. | Mandatory |
| Debtor Account | Indicates the account number of the debtor. This is the nostro account number of the EMI. | Mandatory |
| Debtor Agent BIC/NCC | Indicates the identifier of the agent who is getting debited. This is the identification of the payment bank. | Mandatory |
| Instruction Identification | Indicates the unique identification of the credit transfer initiation request. | Mandatory |
| End to End Identification | Indicates the End to End Identifier of the credit transfer initiation request. | Optional |
| UETR | Indicates the Universally unique identifier of the credit transfer initiation request. | Optional |
| Instruction Priority | Indicates the importance for processing the credit transfer initiation request by payment bank. | Optional |
| Service Level Code/Proprietary | Indicates the agreement under which the credit transfer initiation request must be processed in a coded or proprietary form. | Optional |
| Local Instrument Code/Proprietary | Indicates the local instrument in a coded or proprietary form. | Optional |
| Category Purpose Code/Proprietary | Indicates the high-level purpose of the credit transfer initiation request in a coded or proprietary form. | Optional |
| Instructed Amount & Currency | Indicates the amount requested by the debtor to be transferred to creditor | Mandatory |
| Charge Bearer | Indicates the party that bears the charges associated with the processing of credit transfer initiation request | Optional |
| Ultimate Debtor Name | Indicates the name of the ultimate debtor. This is the name of the EMI customer. | Optional |
| Ultimate Debtor Address | Indicates the Unstructured/Structured address detail of the ultimate debtor. These are the postal address details of the EMI customer. | Optional |
| Ultimate Debtor Identification | Indicates the Identification of the ultimate debtor. This can be BIC, LEI or Organisation Identification of the EMI customer. | Optional |
| Creditor Agent BIC/NCC | Indicates the Identifier of the agent who is getting credited. | Mandatory |
| Creditor Agent LEI | Indicates the legal entity identifier of the agent who is getting credited. | Optional |
| Creditor Agent Name | Indicates the name of the agent who is getting credited. | Optional |
| Creditor Agent Address | Indicates the Unstructured/Structured address detail of the creditor agent. | Optional |
| Creditor Name | Indicates the name of the creditor. | Mandatory |
| Creditor Address | Indicates the Unstructured/Structured address detail of the creditor. | Optional |
| Creditor Identification | Indicates the Identification of the creditor. This could be BIC, LEI, Organisation or Private Identification | Optional |
| Creditor Account | Indicates the IBAN/Account Number of the creditor. | Mandatory |
| Ultimate Creditor Name | Indicates the name of the ultimate creditor | Optional |
| Ultimate Creditor Postal Address | Indicates the Unstructured/Structured address detail of the ultimate creditor. | Optional |
| Ultimate Creditor Identification | Indicates the Identification of the ultimate creditor. This can be BIC, LEI, Organisation or Private Identification of the ultimate creditor | Optional |
| Instruction for Creditor Agent | Indicates the instruction related to processing of the credit transfer initiation request intended for the creditor agent in coded or proprietary form | Optional |
| Regulatory Reporting | Indicates the information relating to regulatory and statutory requirements. | Optional |
| Related Remittance Information | Indicates any information on identification and location of the remittance information | Optional |
| Remittance Information | Indicates the unstructured/Structured remittance information. | Optional |

The Attributes of pain.008.001.08 considered by Temenos Payments Hub is listed below.

| Attribute Name | Description | Mandatory/Optional |
| --- | --- | --- |
| Message Identification | Indicates the message identifier of the pain.008 file. | Mandatory |
| Creation Date Time | Indicates the creation date and time of the pain.008 file. | Mandatory |
| Number of Transactions | Indicates the total number of transactions included in the pain.008 file. | Mandatory |
| Control Sum | Indicates the total value of the transactions included in the pain.008 file. | Optional |
| Initiating Party Name | Indicates the name of the party requesting the payment initiation. This detail is of the EMI implemented in Temenos Payments Hub. | Optional |
| Initiating Party Address | Indicates the unstructured address lines of the party requesting the payment initiation. This detail is of the EMI implemented in Temenos Payments Hub. | Optional |
| Initiating Party BIC | Indicates the identifier of the party requesting the payment initiation. This detail is of the EMI implemented in Temenos Payments Hub. | Mandatory |
| Payment Information Identification | Indicates the Unique identification of the bulk. | Mandatory |
| Payment Method | Indicates the Direct Debit is the supported option to move money between debtor and creditor. | Mandatory |
| Batch Booking | Indicates whether the debtor agent must book a single debit entry per bulk included in the pain.001 or multiple debit entries on the debtor account for transaction included in the bulk. | Optional |
| Number of Transactions per bulk | Indicates the number of transactions included in the bulk. | Optional |
| Control Sum per bulk | Indicates the total value of transactions included in the bulk. | Optional |
| Requested Collection Date | Indicates the date at which the debtor(EMI) requests the payment bank to process the payment. | Mandatory |
| Creditor Name | Indicates the name of the creditor. This is the name of EMI implemented in Temenos Payments Hub. | Optional |
| Creditor Address | Indicates the unstructured address lines of the creditor. This is the postal address line of EMI implemented in Temenos Payments Hub. | Optional |
| Creditor BIC | Indicates the identifier of the creditor. This is the EMI implemented in Temenos Payments Hub. | Mandatory |
| Creditor Account | Indicates the account number of the creditor. This is the nostro account number of the EMI. | Mandatory |
| Creditor Agent BIC/NCC | Indicates the identifier of the agent who is getting credited. This is the identification of the payment bank. | Mandatory |
| Instruction Identification | Indicates the unique identification of the direct debit initiation request. | Mandatory |
| End to End Identification | Indicates the End to End Identifier of the direct debit initiation request. | Optional |
| UETR | Indicates the universally unique identifier of the direct debit initiation request. | Optional |
| Instruction Priority | Indicates the importance for processing the direct debit initiation request by payment bank. | Optional |
| Service Level Code/Proprietary | Indicates the agreement under which the direct debit initiation request must be processed in a coded or proprietary form. | Optional |
| Local Instrument Code/Proprietary | Indicates the local instrument in a coded or proprietary form. | Optional |
| Sequence Type | Indicates the sequence of the direct debit initiation request such as first, recurrent, final or one-off. | Optional |
| Category Purpose Code/Proprietary | Indicates the high-level purpose of the direct debit initiation request in a coded or proprietary form. | Optional |
| Instructed Amount & Currency | Indicates the amount requested by the creditor to be transferred to debtor. | Mandatory |
| Charge Bearer | Indicates the party that bears the charges associated with processing of direct debit initiation request. | Optional |
| Mandate Identification | Indicates the unique identification of the underlying mandate. | Optional |
| Date of Signature | Indicates the date on which the underlying direct debit mandate is signed. | Optional |
| Amendment Indicator | Indicates whether the underlying mandate is amended or not. | Optional |
| Original Mandate Identification | Indicates the unique identification of the original mandate | Optional |
| Original Creditor Scheme Identification Name | Indicates the name of the original creditor | Optional |
| Original Creditor Scheme Private Identification Other Identification | Indicates the original private identification of the creditor | Optional |
| Original Creditor Scheme Private Identification Other Scheme Proprietary | Indicates the original proprietary scheme name for the private identification of the creditor | Optional |
| Original Debtor Account IBAN | Indicates the original IBAN of debtor account. | Optional |
| Original Debtor Agent BIC | Indicates the original BIC of the debtor agent. | Optional |
| Electronic Signature | Indicates the electronic signature of the debtor. | Optional |
| Creditor Scheme Private Identification | Indicates the private identification of the creditor. | Optional |
| Creditor Scheme Private Identification Scheme Proprietary | Indicates the proprietary scheme name for the private identification of the creditor. | Optional |
| Ultimate Creditor Name | Indicates the name of the ultimate creditor. This is the name of the EMI customer. | Optional |
| Ultimate Creditor Address | Indicates the unstructured/Structured address detail of the ultimate creditor. These are the postal address details of the EMI customer. | Optional |
| Ultimate Creditor Identification | Indicates the Identification of the ultimate creditor. This can be BIC, LEI, Organisation Identification of the EMI customer. | Optional |
| Debtor Agent BIC/NCC | Indicates the identifier of the agent who is getting debited. | Mandatory |
| Debtor Agent Address | Indicates the unstructured address detail of the debtor agent. | Optional |
| Debtor Name | Indicates the name of the debtor. | Mandatory |
| Debtor Address | Indicates the unstructured/Structured address detail of the debtor. | Optional |
| Debtor Identification | Indicates the identification details of the debtor such as BIC, LEI, Organisation Identification or Private Identification. | Optional |
| Debtor Account | Indicates the IBAN/Account Number of the debtor. | Mandatory |
| Ultimate Debtor Name | Indicates the name of the ultimate debtor. | Optional |
| Ultimate Debtor Postal Address | Indicates the unstructured/Structured address detail of the ultimate debtor. | Optional |
| Ultimate Debtor Identification | Indicates the identification of the ultimate debtor. This can be BIC, LEI, Organisation or Private Identification of the ultimate debtor. | Optional |
| Purpose | Indicates the purpose of the direct debit initiation request in a coded or proprietary form. | Optional |
| Regulatory Reporting | Indicates the information relating to regulatory and statutory requirements. | Optional |
| Remittance Information | Indicates the unstructured/Structured remittance information. | Optional |

The Attributes of pain.002.001.10 considered by Temenos Payments Hub is listed below.

| Attribute Name | Description | Mandatory/Optional |
| --- | --- | --- |
| Message Identification | Indicates the message identifier of the pain.002 file. | Mandatory |
| Creation Date Time | Indicates the creation date and time of the pain.002 file. | Mandatory |
| Initiating Party BIC | Indicates the identifier of the party sending the status report. This detail is of the payment bank. | Optional |
| Original Message Identification | Indicates the message identifier of the pain.001/pain.008 file. | Mandatory |
| Original Message Name Identification | Indicates the original message name identifier. This could be pain.001 or pain.008 | Mandatory |
| Group Status | Indicates the overall status of the pain.001or pain.008 file. When group status is accepted, bulk level and transaction level information is not expected. When group status is partially accepted or rejected, further details on the rejected transaction are expected at bulkor transaction level. | Mandatory |
| Group Status Reason | Indicates the reason for rejection of the pain.001/pain.008 file in coded or proprietary form. Reason must be specified in case the group status is rejected. | Optional |
| Original Payment Information Identification | Indicates the identifier of the original bulk included in pain.001/pain.008. | Optional |
| Original Control Sum | Indicates the total value of the transactions included in the bulk. | Optional |
| Payment Information Status | Indicates the status of the bulk. | Optional |
| Payment Information Status Reason | Indicates the reason for rejection of the bulk in coded or proprietary form. Reason must be specified in case the payment information status is rejected. | Optional |
| Detailed Number of Transactions Per Status | Indicates the total number of transactions which are accepted and rejected in the bulk. | Optional |
| Detailed Control Sum per Status | Indicates the total value of transactions which are accepted and rejected in the bulk. | Optional |
| Transaction Status Identification | Indicates the identification for the status information as received from payment bank. | Optional |
| Original Instruction Identification | Indicates the unique identification of the original credit transfer initiation or direct debit initiation request. | Optional |
| Original End to End Identification | Indicates the End to End Identifier of the original credit transfer initiation or direct debit initiation request. | Optional |
| Original UETR | Indicates the universally unique identifier of the original credit transfer initiation or direct debit initiation request. | Optional |
| Transaction Status | Indicates the status of the transaction. Only rejected status is indicated here. | Optional |
| Transaction Status Reason | Indicates the reason for rejection of the transaction in coded or proprietary form. Reason must be specified in case the transaction status is rejected. | Optional |
| Original Transaction Amount | Indicates the original amount and currency indicated in the credit transfer initiation or direct debit initiation request. | Optional |
| Original Debtor Agent BIC/NCC | Indicates the original identifier of the agent who is getting debtor. | Optional |
| Original Creditor Agent BIC/NCC | Indicates the original identifier of the agent who is getting credited. | Optional |

The Attributes of camt.054.001.10 considered by Temenos Payments Hub is listed below.

| Attribute Name | Description | Mandatory/Optional |
| --- | --- | --- |
| Message Identification | Indicates the message identifier of the camt.054 file. | Mandatory |
| Creation Date Time | Indicates the creation date and time of the camt.054 file. | Mandatory |
| Credit Debit Indicator | Indicates whether the notification is for a credit or debit entry. | Mandatory |
| Transaction Amount & Currency | Indicates the amount and currency of the underlying transaction for which notification is sent by the payment bank. | Mandatory |

The below attributes are not used for processing the received camt.054 but it is stored in Temenos Payments Hub in *local reference*.

| Attribute Name | Description | Mandatory/Optional |
| --- | --- | --- |
| Notification Identification | Indicates the unique identification of the notification. | Optional |
| Account Number | Indicates the account number which is credited/debited. This is the EMI account. | Optional |
| Entry Reference | Indicates the unique reference of the entry. | Optional |
| Entry Status Code | Indicates the status of the entry. | Optional |
| Value Date | Indicates the value date of the underlying transaction. | Optional |
| Bank Transaction Code | Indicates the type of the underlying transaction in coded or proprietary form. | Optional |
| Transaction Message Identification | Indicates the Unique identification of the message containing the underlying transaction. | Optional |
| End to End Identifier | Indicates the End to End identifier of the underlying transaction. | Optional |
| UETR | Indicates the universally unique identifier of the underlying transaction. | Optional |
| Transaction Identification | Indicates the Transaction identification of the underlying transaction. | Optional |
| Mandate Identification | Indicates the unique identification of the underlying mandate. | Optional |
| Charge Information | Indicates the Information related to charges applicable on the underlying transaction such as amount, currency, bearer, and charge agent. | Optional |
| Debtor Details | Indicates the Name, BIC, LEI, Organisation, or Private Identification of the debtor in the underlying transaction. | Optional |
| Debtor Account | Indicates the IBAN or account number of the debtor in underlying transaction. | Optional |
| Ultimate Debtor | Indicates the information on ultimate debtor in the underlying transaction such as Name, BIC, LEI, Organisation or Private Identification. | Optional |
| Creditor Details | Indicates the Name, BIC, LEI, Organisation, or Private Identification of the creditor in the underlying transaction. | Optional |
| Creditor Account | Indicates the Name, BIC, LEI, Organisation, or Private Identification of the creditor in the underlying transaction. | Optional |
| Ultimate Creditor | Indicates the IBAN or account number of the creditor in underlying transaction. | Optional |
| Debtor Agent BIC/NCC | Indicates the Identifier of the agent who is getting debited in the underlying transaction. | Optional |
| Creditor Agent BIC/NCC | Indicates the Identifier of the the agent who is getting credited in the underlying transaction. | Optional |
| Local Instrument | Indicates the local instrument of underlying transaction in coded or proprietary form. | Optional |
| Category Purpose | Indicates the High-level purpose of the underlying transaction in coded or proprietary form. | Optional |
| Purpose | Indicates the reason for the underlying transaction in coded or proprietary form. | Optional |

In this topic

- [Introduction to C2B Message Exchange](#IntroductiontoC2BMessageExchange)

- [Supported Message Formats](#SupportedMessageFormats)
- [Initiating Credit Transfer Requests](#InitiatingCreditTransferRequests)
- [Outward Processing of Credit Transfer Initiation Request to Payment Bank](#OutwardProcessingofCreditTransferInitiationRequesttoPaymentBank)
- [Initiating Direct Debit Collection Requests](#InitiatingDirectDebitCollectionRequests)
- [Outward Processing of Direct Debit Initiation Request to Payment Bank](#OutwardProcessingofDirectDebitInitiationRequesttoPaymentBank)
- [Bulking Criteria](#BulkingCriteria)
- [Channel Validations](#ChannelValidations)
- [Handling Status Report for Credit Transfer Initiation and Direct Debit Initiation Request](#HandlingStatusReportforCreditTransferInitiationandDirectDebitInitiationRequest)
- [Matching to Original Transaction](#MatchingtoOriginalTransaction)
- [Receiving Debit Credit Notifications from Payment Bank](#ReceivingDebitCreditNotificationsfromPaymentBank)
- [Supported Attributes](#SupportedAttributes)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 6:04:44 PM IST