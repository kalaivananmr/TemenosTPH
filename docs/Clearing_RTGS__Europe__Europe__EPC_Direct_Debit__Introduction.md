# Introduction to EPC SEPA Direct Debit

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/EPC_Direct_Debit/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [EPC SEPA Direct Debit](../../Europe/EPC_Direct_Debit/Introduction.htm) > Introduction

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
    - [Introduction](../../Europe/EPC_Direct_Debit/Introduction.htm)
    - [Configuration](../../Europe/EPC_Direct_Debit/Configuration.htm)
    - [Working with](../../Europe/EPC_Direct_Debit/Working_with.htm)
    - [Tasks](../../Europe/EPC_Direct_Debit/Tasks.htm)
    - [Outputs](../../Europe/EPC_Direct_Debit/Outputs.htm)
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

# Introduction to EPC SEPA Direct Debit

Updated On 10 July 2025 |
 50 Min(s) read

Feedback
Summarize

EPC Direct Debit (EPC DD) is a clearing module in Temenos Payments Hub (TPH) that is compliant with EPC guidelines for SEPA Direct Debits (SDD). This module is offered as an upgrade path for clients to migrate to TPH. Clients can use this module to configure the local clearing in TPH in a comparatively shorter time frame as the module is already compliant with EPC, the module thereby acting as an accelerator for the upgrade.

- License for the module is PPEPCP.
- The EPC Direct Debit feature is compliant with ‘SEPA Direct Debit B2B Inter-PSP Implementation Guidelines 2025 Version 1.0’ and ‘SEPA Direct Debit Core Inter-PSP Implementation Guidelines 2025 Version 1.0’ specifications.

Read [Direct Debits](../../../../Payments/PP/Payments_Hub_(PP)/Direct_Debits/Introduction.htm) for more information on SEPA Direct Debit and its uses.

## Types of Payment and Messages

TPH supports the following SEPA DD message types:

| Business Event | Transaction Type | Description | ISO Message | Version |
| --- | --- | --- | --- | --- |
| DD transfer initiation | DD | - Receives and executes customer-to-bank DD collection requests. - Validates the request received from the creditor and routes it through appropriate clearing (when the debtor belongs to another bank), based on the Requested Collection Date (RCLD), cut-off time, and days required for the clearing to finally settle the amount. - Warehouses the payments with a future value date and processes on the due date. - Forwards the finalised payment to clearing in pacs.003 message format. - Raises settlement entries at the RCLD or settlement date. | pain.008 or initiated through PP.ORDER.ENTRY (OE) DD book or outgoing page | 08 |
| DD | DD | - Receives and processes bank-to-bank DD payment orders to debit the debtor in the books of the processing bank. - Executes DD successfully, when:   - Debit instruction is received with appropriate mandates.   - Debtor account has sufficient funds. - Otherwise, the debit item is rejected or returned. | pacs.003 | 08 |
| DD reject | RJ | - A negative confirmation of direct debit item received by the debtor bank. - TPH performs the following:   - Sends an outbound DD rejection message (pacs.002), when DD instruction from clearing cannot be processed successfully (for example, the debtor mandate is not available and funds are insufficient in the debtor account).   - Receives inbound DD reject message (pacs.002) and marks the previously sent collection item as Rejected (which are excluded for Settlement). | pacs.002 | 10 |
| Return debit transfer or DD | RF | - Enables the return of DD after the settlement date, when it is within the allowed time period of the clearing.  The return debit transfer or DD event is initiated by the debtor bank. - TPH performs the following:   - Supports automated and manual returns of incoming DDs that are unsuccessful.   - Generates pacs.004 outgoing returns to clearing.   - Supports DD returns received by the creditor bank for previously originated debits.   - Receives the returns as pacs.004 messages and process them as Straight Through Processing (STP). | pacs.004 | 09 |
| Debit refunds | RD | - DD can be returned manually at the request of the debtor, within the allowed time period when supported by the clearing. - TPH performs the following:   - Generates pacs.004 message for outgoing DD refunds.   - Supports receipt of DD refunds from debtor bank by using clearing and processes them by debiting the creditor who initiated the DD. | pacs.004 | 09 |
| Customer payment (DD) reversal | RV | - Creditor bank can receive a payment (DD) reversal request (pain.007 message) from the creditor. - TPH performs the following:   - Supports the receipt of customer payment reversal message (pain.007) to reverse a previously initiated DD.   - Processes the accepted reversals as STP by debiting the creditor (initiating the reversal) and crediting the beneficiary.   - Generates an outgoing pacs.007 message for DD reversals to clearing. | pain.007 or initiate a reversal of a processed DD through OE | 09 |
| DD reversal | RV | Receives DD reversals (pacs.007) and credits the debtor account.  Debtor bank can receive an incoming DD reversal from the creditor bank through clearing. | pacs.007 | 09 |

## Processing Post and Pre-Settlement DD

Temenos Payments Hub supports the processing of,

- Pre-Settled Direct Debit (for example, BACS) instructions – Settlement transaction is created during message generation.
- Post-Settled Direct Debit (for example, SEPA DD) instructions – Settlement transaction is generated on the requested collection date.

[Pre-Settlement](#)

The SEPA DD is initiated and sent for pre-settlement clearing in one interbank business day and a maximum of 14 days before the request collection or settlement date). The SEPA DD is settled and the settlement booking entries to the clearing Nostro account occur on the settlement date (RCLD). The settlement is done considering all the rejections until the settlement date. One of the following actions can be performed on a DD before the clearing reject cut-off (pre-settlement).

- Canceled by the creditor’s bank
- Rejected by the debtor’s bank
- Refused by the debtor through the debtor bank

[Post-Settlement](#)

After clearing the settlement, one of the following actions can be performed on the processed DD (processed or completed and settled by the clearing).

- Initiating DD reversal by creditor bank
- Return by the debtor bank
- Refund by the debtor (through debtor’s bank)

The debtor can set a period to avail a refund depending on the authorisation or unauthorisation of DD mandate.

## SEPA DD Schemes

There are two types of schemes in SEPA DD,

- B2B
- CORE

To choose a DD scheme, the user must provide the *Local Instrument Code* in PP.ORDER.ENTRY as B2B or CORE.

| Scheme | User | Description |
| --- | --- | --- |
| SEPA Direct Debit B2B | Business | - SDD B2B payments usually occur between businesses (but the creditor can be an individual customer). - Payment Service Provider (PSP) participation is optional. - The debtor PSP must maintain the mandate and check its validity while processing collection requests according to the SDD rule book. - The refund option is not available to the debtor after the SDD is processed successfully. |
| SEPA Direct Debit CORE | Consumer | - SDD core payments take place between customers and businesses. - PSP participation is mandatory. - The debtor banks may check the mandates as an additional or optional service while processing collection requests. - The refund option is available for the debtor even after SDD is processed successfully. |

Both the SEPA DD schemes operate in Euro. However, the following can be different for each scheme.

- Timelines in which SDD business events occur.
- Configuration of timelines and mandate verification (by debtor bank).

## Processing DD Batches and Single DD

TPH supports DD batch and single DD processing.

[DD Batch Processing](#)

The user must set *BatchBooking* as True to initiate a DD batch and bulk it in a pain.008 message bulk. If *BatchBooking* is not set in the pain.008 message, the user configures the *BatchBooking* as True (as part of a Netting agreement configured for the submitter of the bulk or default Netting agreement). A pain.008 file has multiple DD batches (bulks) with different RCLD. The system processes the DD batch as follows:

- One parent transaction for crediting the creditor’s account and debiting a batch suspense (wash) account with the total amount of DD in the message bulk.
- Child transaction for each DD in the batch,
  - Debiting the debtor’s account (in-book transaction) or clearing suspense account (outgoing transaction).
  - Crediting the batch suspense (wash) account with the individual DD amount.

[Single DD Processing](#)

The user must set *BatchBooking* as False to initiate a single DD and bulk it in a pain.008 message bulk. If *BatchBooking* is not set in the pain.008 message, the user configures the *BatchBooking* as False (as part of a Netting agreement). The system creates a single transaction for each DD in the batch,

- Debiting the debtor’s account (for book transaction) or clearing suspense account (outgoing transaction).
- Crediting the creditor’s (client) account with the individual DD amount.

## Processing Recurrent and One-Off DD

The SEPA DD processes both recurrent (RCUR) and one-off (OOFF) transactions based on the Mandate Type and Sequence Type in the DD.

| Type | Description |
| --- | --- |
| Recurrent DD | Debtor’s authorisation is used for regular DD initiated by the creditor. |
| One-off DD | Debtor’s authorisation is given only once to collect one single DD. This cannot be used for any subsequent transaction. |

TPH supports the validation of both the DDs.

## Validating SDD Mandate

The debtor bank validates an SDD mandate provided in an incoming DD collection when configured in PP.CLEARING.SETTING for the respective DD scheme (CORE or B2B). Read [Mandate Validation and Auto-registration of Mandate](../../../../Payments/PP/Payments_Hub_(PP)/Direct_Debits/Introduction.htm#Mandate_Validation_and_Auto-registration_of_Mandate), [Mandate Limit Check, and Creditor Restrictions](../../../../Payments/PP/Payments_Hub_(PP)/Direct_Debits/Introduction.htm#Mandate_Limit_Check_and_Creditor_Restrictions) for more information.

The following attributes of the mandate available in an incoming SEPA DD message are compared to the mandate in the mandate administration (DD.DDI):

- *Identification Code of the Scheme* (B2B or CORE)
- *Unique Mandate Reference*
- *Identifier of the Creditor* (*Creditor ID*)
- *Account Number of the Debtor (IBAN)*
- *BIC Code of* *Debtor Bank*
- *Transaction Type*

All the attributes in the list needs to be identical, except *Transaction Type*.

If recurrent collection is available for one-off mandate, it does not cover the successive collections available after the first collection. In addition to the above attributes, the following factors are checked for each mandate of a SEPA DD collection:

- Mandate is not canceled by the debtor or creditor.
- Collection must not exceed the maximum number of transactions.
- Mandate must not exceed the maximum amount of the collection.
- Mandate complies with the periodicity setup in the mandate administration (available only on certain days of the month or week).

## SEPA Direct Debit R-Transactions

Participant PSPs must manage exceptions that arise when one of the parties involved in a DD transaction is unable to process a collection request. In such cases, the PSP must initiate or receive rejects, returns, refunds, and reversals, collectively called R-transactions.

The type of R-transaction depends on the initiator of the message and the point at which the R-transaction is initiated. The below diagram explains the type of R-message based on time and party of initiation. Temenos Payments Hub allows the participant PSPs to manage the messages depicted in the diagram.



According to the SDD scheme guidelines, participants must channel rejects, returns, reversals, and refunds of SDD collections through the same Clearing and Settlement Mechanism (CSM) used for the original SDD collection, unless agreed by the SDD scheme participants.

## Pre-Settlement SDD Events or Messages

The below table portrays SEPA DD events or messages before clearing settlement as a set of steps and events in the order of occurrence. It includes all the rejects, refusals, or cancellation requests of a DD transaction (pre-settlement R-messages).

| Business Event or Timeline | Creditor | <--> | Creditor Bank | <--> | Clearing Settlement at Settlement Date (D) | <--> | Debtor Bank | Debtor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD initiated: <RCLD-14C | Initiate DD | --> pain.008 | Warehouses and releases at RCLD-14C | --> pacs.003 | Scheduled at D=RCLD | --> pacs.003 | Receives at D-14 | Option for refusal |
| DD initiated: > RCLD-14C and <= RCLD-1TD | Initiate DD | --> pain.008 | Validates and sends the message to clearing on the same day. DD scheduled at due date or book date = RCLD | --> pacs.003 | D=RCLD | --> pacs.003 | Receives on the same day, the creditor initiates the DD | Option for refusal |
| DD initiated: RCLD | Initiate DD | --> pain.008 | Validates and sends the message to clearing on the same day. DD scheduled at due date = RCLD+1C | --> pacs.003 (with RCLD = RCLD+1C) | D = RCLD+1 | --> pacs.003 | Receives on the same day, the creditor initiates the DD | Option for refusal |
| DD refused by debtor: <= D before reject cut-off |  | <-- pain.002 (optional based on configuration) | Rejects DD transaction. Does not settle register transaction at D | <--pacs.002 | Does not settle register transaction at D | <--pacs.002 | Refusal message initiated on behalf of the debtor | Request for refusal to the bank |
| DD reject by debtor bank: <=D before reject-cutoff |  | <-- pain.002 (optional based on configuration) | Rejects DD transaction. Does not settle register transaction at D | <--pacs.002 | Does not settle register transaction at D | <--pacs.002 | Rejects message initiated on behalf of the debtor bank |  |
| DD cancellation request by creditor bank:  <= D before reject-cutoff |  |  | Initiates cancellation request on behalf of creditor or bank | --> camt.056 | Does not settle register transaction at D | --> camt.056 | Rejects DD transaction. Do not settle register transaction at D |  |
| Settlement at D | Creditor account debited |  | Books clearing settlement transaction |  | Settled at D or D+1TD (when D is not a banking business day) |  | Clearing settlement transaction booked | Debtor account debited |

The description of the values are:

| Value | Description |
| --- | --- |
| RCLD | Requested collection date available in a pain.008 DD transaction |
| C | Calendar days (for example, 14C = 14 calendar days) |
| D | Clearing settlement date of the pain.008 bulk |
| TD | Target days (Interbank business days) |
| DD | Direct debit |

- A DD transaction booked at D cannot be rejected by debtor bank, refused by debtor, or cancelled through cancellation request by creditor bank.
- If D is a local bank holiday, the debtor is debited at D + 1 banking business day.

The clearing settlement transaction is booked at D as follows:

| Type of Bank | Account | Note |
| --- | --- | --- |
| Creditor bank | - Debit – Clearing account (Nostro) - Credit – Clearing suspense account | Total requested settlement amount of the outgoing pacs.003 bulk. |
| Debtor bank | - Debit – Clearing suspense account - Credit – Clearing account (Nostro) | Total requested settlement amount of an incoming pacs.003 bulk is subtracted with any rejected DD transactions (by the debtor bank or on behalf of a refusal from the debtor). |

## Post-Settlement SDD Events or Messages

The below table displays the post-settlement events or messages as a set of steps that occur after clearing settlement of the DD. The timeline mentioned for each business event, in which the event can differ for CORE and B2B DD.

| Business Event or Timeline | Creditor | <--> | Creditor Bank |  | Clearing Settlement | <--> | Debtor Bank | Debtor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD return by Debtor bank:  - For CORE: <= D+5TD - For B2B: <= D+3TD | Debited with original amount of original DD transaction. |  | Books clearing settlement transaction. | <--pacs.004 | Receives the forward return that is settled on the date of return. This is the interbank settlement date in pacs.004. | <--pacs.004 | Initiates return message and sends it to clearing. Books clearing settlement transaction. | Credits debtor account with original amount of original DD transaction returned. |
| DD refund by debtor for authorised debit mandate:  - For CORE:<= D+ 8 weeks - For B2B: No refund option | Debited with original amount of original DD transaction. |  | Books clearing settlement transaction. | <--pacs.004 | Receives the forward return that is settled on the date return. This is the interbank settlement date in pacs.004. | <--pacs.004 | Initiates return message and sends it to clearing. Books clearing settlement transaction. | Credits debtor account with original amount of original DD transaction returned. |
| DD reversal by creditor: <= D+5TD | Debited with the amount of the reversal of a settled collection. | -->pain.007 | Validates and sends reversal to clearing, on the date it receives the reversal. Books clearing settlement transaction. | -->pacs.007 | Receives the forward reversal that is settled on the date reversal. | -->pacs.007 | Credits debtor account with the amount of the reversal. Books clearing settlement transaction. | Credits debtor account with the amount of the reversal of a settled collection. Book date or credit value date is configurable (no limitation by the scheme). |

The description of the values are:

- D – Clearing settlement date of the pacs.003 bulk
- TD – Target days (Interbank business days)

The default timelines for return and refund of a DD are provided below.

| Date for Settlement | Scheme | Day |
| --- | --- | --- |
| Return | CORE | 5 interbank business days (after the settlement date of the collection available to the debtor bank) |
| B2B | 3 interbank business days (after the settlement date of the collection available to the debtor bank) |
| Refund | CORE | 8 weeks + 2 TD interbank business days (after the settlement date of the collection available to the debtor bank) |
| B2B | Not allowed or supported in the scheme |

The system checks the timeline for incoming DD return or refund, and routes the transaction to the Repair queue (if timeline is exceeded).

| Type of Bank | Refund | Reversal |
| --- | --- | --- |
| Creditor Bank | A clearing settlement transaction is booked as follows for return or refund messages:  - Debit – Clearing suspense account - Credit – Clearing account (Nostro)   Total requested settlement amount of the incoming pacs.004 bulk. | A clearing settlement transaction is booked as follows for reversal messages:  - Debit – Clearing suspense account - Credit – Clearing account (Nostro)   Total requested settlement amount of the outgoing pacs.007 bulk. |
| Debtor Bank | A clearing settlement transaction is booked as follows for return or refund messages:  - Debit – Clearing account (Nostro) - Credit – Clearing suspense account   Total requested settlement amount of the outgoing pacs.004 bulk. | A clearing settlement transaction is booked as follows for reversal messages:  - Debit – Clearing account (Nostro) - Credit – Clearing suspense account   Total requested settlement amount of the incoming pacs.007 bulk. |

## Bulking Criteria

The outgoing SEPA DD files sent for clearing are bulked with the same message types (but different for CORE and B2B). However, the transactions are grouped in a message bulk based on the following bulking criteria.

| Message | Description |
| --- | --- |
| pacs.003 | RCLD (calculated debit value date of the DD) |
| pacs.004 | Interbank settlement date (calculated debit value date of the DD return) |
| pacs.007 | Processing date (credit value date of the DD reversals) |
| pacs.002 | Processing date (date of the reject or refusal) |

## Outward Processing of DD Initiation

This section describes the outward processing of a DD order initiated in TPH or ordering bank.



| Activity | Description |
| --- | --- |
| Manual capture of SEPA DD initiation from branch or back office by using OE page | - Captures a SEPA DD from TPH OE page. - Validates (mandatory and non-mandatory) fields and inputs data on submission. |
| Outgoing DD payment instructions through ordering bank | - Sends DD payment instructions to TPH bank through ordering party’s bank (same as TPH bank or another bank). - The instruction is in the pain.008.001.08 – ISO20022 format. |
| File duplicate check | - Checks whether a file is received from a channel other than TPH OE. - Rejects duplicate files and sends a negative pain.002 message to the initiating bank or system (if configured). - This check is based on the following combination of fields in the pain.008 file.   - Group header message identification   - Message format of the file   - Group header initiating party organisation ID BIC   - Source from which the pain.008 file is originated |
| Format validation | Validates the pain.008 message format by checking mandatory and non-mandatory fields, proper field length, and content based on pain.008.001.08 XML definition language. |
| Bulk agreement validation | - Validates pain.008 bulks against a netting agreement setup for the submitter of the bulk. - To perform this, navigate to **Admin Menu** > **Payment Hub** > **Debit Authority** > **Netting Agreements**.   - Netting agreement validation can be skipped when *MessageType* (pain.008) is configured in the No DA List (in the **Debit Authority** menu). - Bulk agreement validation is not applied for DD initiated from TPH OE page. |
| Credit account validation | Validates if the ordering account,  - Is a valid Temenos Transact account - Has a posting restriction |
| Execution warehouse | Warehouse DD initiations that are received 14 calendar days (or more) prior to the RCLD (which is configured in *MaxAllowedDays* in PP.SOURCE.SETTING) or scheduled for release on RCLD minus 14 calendar days. The following is performed in a DD batch that is received 14 calendar days (or more) before RCLD:  - Warehouses the parent (total amount) transaction. - Creates child transactions from the batch when the parent transaction is released and validates it successfully. |
| Determine SEPA outgoing clearing | - Determines the outgoing clearing channel from the RS Channel Selection List. - To access this, navigate to **Admin Menu** > **Payment Hub** > **Routing and Settlement**. - The clearing suspense account is determined for the respective outgoing SEPA clearing channel (for example, local clearings such as STET, DIAS). |
| Reachability check | Validates if the debtor bank (BIC) is reachable through the selected SEPA clearing. Read [Reachability](../../../../Orders/PI/Payment_Initiation_(PI)/Reachability/Introduction.htm) for more information. |
| EPC common payment validations | Performs this validation on the DD to ensure that it meets the EPC guidelines. The following fields are must be validated.   - *Transaction Amount* - *Details of Charges (needs to be equal to SHA or SLEV)* - *RCLD* - *Mandate Identification* - *Mandate Date Of Signature* - *Creditor Scheme ID* - *Creditor Name* - *Debtor Name*   Following are the exclusions in the EPC common payment validations:   - Currency must be EUR. - Debtor and Creditor IBAN is mandatory. - Debtor agent and Creditor agent BIC is mandatory. |
| Local Clearing channel validations | Banks add local clearing-specific validations along with the EPC common payment validations. |
| Dates calculation | - Calculates the DD (debit and credit) value dates and booking dates. The basic rules for date calculation for outgoing transactions are as follows.   - If the RCLD of the DD initiation is equal to or before the current business date, the settlement date is set to one banking business date ahead of the current business date. This is based on the configured settlement shift for the respective SEPA clearing, which is one day for both CORE and B2B DD scheme.   - If the clearing cut-off time elapses when applying the settlement shift, the system applies another cut-off shift day (one day). - Allows to configure the settlement and cut-off shifts through **Admin Menu** > **Payment Hub** > **Routing and Settlement** > **Channel Cut-off Configuration**. - Calculates the debit and credit value dates and book date, which is equal to determined collection or settlement date. |
| Duplicate check | Configures the check based on the following criteria:   - DD batch booking (parent transaction that books the total amount)   - *Account of the Credit Party*   - *Currency of the Credit Account*   - *Transaction Amount*   - *Currency*   - *RCLD*   - *Bulk Reference* - Each DD transaction in a batch   - *Account of the Debit Party*   - *Currency of the Debit Account*   - *Transaction Amount*   - *Transaction Currency*   - *RCLD*   - *Instruction Identification* - Single outgoing DD transaction (*BatchBooking* is false)   - *Account of the Credit Party*   - *Currency of the Credit Account*   - *Transaction Amount*   - *Transaction Currency*   - *RCLD*   - *Instruction Identification*   The user can configure the duplicate checks if required. |
| Filtering | Filters the payments when interfaced with a screening engine. This is a bank-specific requirement and is performed in the site.  Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Generate and send pacs.003 to clearing | Bulks DD initiations and sends a pacs.003 message to the respective SEPA clearing when,   - DD transactions are received at least 14 days before the given RCLD. - All business validations are qualified. |
| Warehouse future dated | Warehouses DD initiations or schedules for release on the calculated debit value date (which is equal to the settlement or collection date). |
| Fees calculation | Charges creditor for any fees.  Fees for child DD transactions are posted separately (like single DD transactions) from the batch parent transactions. |
| Posting | Credits the creditor’s account with the transaction amount.  If the posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or is canceled. Read [Error queue](#Errorqueue) for more information.  **Posting**   - If a DD initiation is a child of a batch (booking indicator is true or configured as a part of the netting agreement), then:   - Debit clearing suspense account is configured in PP.CLEARING.SETTING   - Credit batch suspense account is configured for each company - If a DD initiation is a single transaction (booking indicator is false or configured as a part of the netting agreement), then:   - Debit clearing suspense account is configured in PP.CLEARING.SETTING   - Credit creditor is the ordering client - Total requested bulk amount of a batch booking transaction is known as the parent transaction of the batch children, in which:   - Batch suspense account is configured for each company   - Credit creditor is the ordering client   **Settlement Booking Entry**   - If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Error queue | - Rejects batch child transactions with validation errors by performing the following posting on the settlement or collection date.   - Debit creditor is the ordering client.   - Credit batch suspense account is configured for each company. - Routes single or parent transaction (parent books the total amount of the batch) with validation errors to the Repair queue for user intervention or cancels them automatically.  Automatic cancellation is available only for TPH. - Routes invalid batch children to the Repair queue similar to single DD that is based on the specific configuration in PP.NETTING.AGREEMENT (*RepairBatchChild* is set as Y). |

## Book Processing of DD Initiation

This section describes the processing of a DD book order initiated in TPH or ordering bank.



| Activity | Description |
| --- | --- |
| Manual capture of SEPA DD initiation from branch or back office by using OE page | - Captures a SEPA DD from TPH OE page. - Validates mandatory and non-mandatory fields and inputs the data on submission. |
| Outgoing DD payment instructions through ordering bank | Sends DD payment instructions to TPH bank through ordering party’s bank (same as TPH or another bank). The instruction is in pain.008.001.08 – ISO20022 format. |
| File duplicate check | - Checks if a file is received from a channel other than PAYMENT.ORDER or TPH OE. - Rejects the file (if it is a duplicate) and sends a negative pain.002 message to the initiating bank or system (if configured). - This check is based on the following combination of fields in the pain.008 file:   - Group header message identification   - Message format of the file   - Group header initiating party organisation Id BIC   - Source from which the pain.008 file is originated |
| Format validation | Validates the pain.008 message format by checking mandatory and non-mandatory fields, proper field length, and content based on pain.008 XML definition language. |
| Bulk agreement validation | Validates pain.008 bulks against a netting agreement setup for the submitter of the bulk through **Admin Menu** > **Payment Hub** > **Debit Authority** > **Netting Agreements**.  - Netting agreement validation can be skipped when the *MessageType* (pain.008) is configured in the No DA List (in the **Debit Authority** menu). - Bulk agreement validation is not applied for DD initiated from TPH OE page. |
| Credit account validation | Validates if the ordering account,  - Is a valid Temenos Transact account. - IHas a posting restriction. |
| Execution warehouse | Warehouses DD initiations that are received 14 calendar days (or more) prior to the RCLD (which is configured in *MaxAllowedDays* in PP.SOURCE.SETTING) or scheduled for release on RCLD minus 14 calendar days. The following is performed in a DD batch that is received 14 calendar days (or more) before RCLD:  - Warehouses the parent (total amount) transaction - Creates child transactions from the batch when the parent transaction is released and validates it successfully |
| Debit account validation | Validates if the debtor account,   - Is a valid Temenos Transact account - Has a posting restriction |
| Dates calculation | - Calculates the DD (debit and credit) value dates and booking dates.   - If the RCLD of the DD initiation is equal to or before the current business date, the settlement date is set to one banking business date ahead of the current business date. This is based on the configured settlement shift for the respective LEDGER, which is one day for both CORE and B2B scheme DD.   - If the clearing cut-off time has passed when applying the settlement shift, the system applies another cut-off shift day (1 day). - Allows to configure the settlement shift and cut-off shift through **Admin Menu** > **Payment Hub** > **Routing and Settlement** > **Channel Cutoff Configuration**.   Calculates the debit and credit value dates and book date, which equals the determined settlement date. |
| Duplicate check | Enables to configure the check based on the following criteria: DD batch booking (parent transaction that books the total amount)   - *Account of the Credit Party* - *Currency of the Credit Account* - *Transaction Amount* - *Currency* - *RCLD* - *Bulk Reference*   Each DD transaction in a batch   - *Account of the Debit Party* - *Currency of the Debit Account* - *Transaction Amount* - *Transaction Currency* - *RCLD* - *Transaction Identification*   Single book DD transaction (*BatchBooking* is false in the DD)   - *Account of the Credit Party* - *Currency of the Credit Account* - *Account of the Debit Party* - *Currency of the Debit Account* - *Transaction Amount* - *Transaction Currency* - *RCLD* - *Transaction Identification*   The user can configure the duplicate checks. |
| Warehouse future dated | Warehouses DD initiations or schedules release on the calculated debit value date (which is equal to settlement date). |
| Fees calculation | Charges creditor and debtor for any fees (if configured). Fees for child DD transactions are posted (like single DD transactions) and not along with the batch parent transaction). |
| Balance check | Checks if sufficient funds are available in the debtor’s account before posting a DD transaction (child of a batch or single DD).  - If sufficient funds are not available, it performs the following:   - Cancels or rejects the DD transaction (automatically)   - Routes to the Repair queue   - Retries checking till the RCLD or settlement date. The system is configured to retry debiting the debtor’s account even a few days after the settlement date (based on *SettlementRetryDays* configured as part of a netting agreement). - If sufficient funds are not available in the debtor’s account on the settlement date and after the settlement retry days, the system rejects the DD. |
| Posting | Credits the creditor’s account with the transaction amount. If posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or cancels it. Read [Error queue](#Errorqueue) for more information. **Posting**   - If a DD initiation is a child of a batch (batch booking indicator is true or configured as a part of the netting agreement), then:   - Debit clearing suspense account is configured in PP.CLEARING.SETTING   - Credit batch suspense account is configured for each company) - If a DD initiation is a single transaction (batch booking indicator is false or configured as a part of the Netting Agreement), then:   - Debit clearing suspense account is configured in PP.CLEARING.SETTING   - Credit creditor is the ordering client - Total requested bulk amount of a batch booking transaction is known as the parent transaction of the batch children, in which:   - Batch suspense account is configured for each company   - Credit creditor is the ordering client   **Settlement Booking Entry**  If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Error queue | - Rejects batch book child transactions with validation errors by performing the following posting on the settlement date:   - Debit creditor is the ordering client   - Credit batch suspense account is configured for each company - Routes single transactions or DD parent transactionswith validation errors to the Repair queue for user intervention or cancels them automatically.  - Automatic cancellation is available only for TPH.   - Additionally, it routes invalid batch children to the Repair queue based on specific configuration as part of a Netting Agreement (*RepairBatchChild* is set to Y). |

## Inward Processing of SEPA DD from Clearing

This section describes the processing of an incoming DD from a SEPA clearing initiated by the creditor’s bank.



| Activity | Description |
| --- | --- |
| Message format validation | Validates pacs.003 message format by checking mandatory and non-mandatory fields, proper field length and content based on pacs.003 XML definition language file (provided by the clearing). |
| Mandate validation | Validates the mandate for B2B DD and amends it (when *MandateAmendmentIndicator* is enabled in PP.CLEARING.SETTING configuration and the amendment information is provided with DD).  - In Core DD, the mandate validation is optional (according to the scheme) and auto-mandate creation is activated. - If the mandate does not exist in DD.DDI, canceled, expired, or exceeds the limit (based on periodicity and maximum amount), the system routes the DD to repair or rejects it.   Read [Repair](#Repair) or [Automated reject processing](#AutoRejProc) for more information. |
| Debit account validation | - Validates if the debit account is a valid Temenos Transact account. - Routes the DD to repair (or rejects automatically) if the account is invalid, frozen, closed, or does not exist.   Read [Repair](#Repair) or [Automated reject processing](#AutoRejProc) for more information. |
| Dates calculation | Determines the settlement date (as the RCLD is from the inward DD).  - If the RCLD is equal to or before the current business date, the settlement date is set to the current business date. - If the determined settlement date is a bank holiday, the system forwards the date to the first banking business day based on the cut-off shift day. - Allows to configure one day in channel cut-off through **Admin Menu** > **Payment Hub** > **Routing And Settlement** > **Channel Cut-off Configuration**.   Calculates the debit and credit value dates and book date, which equals the determined settlement date. |
| Duplicate check | Enables to configure the check on the following:  - *End-To-End Reference* (Customer Specified Reference) - *RCLD* - *Mandate Reference* - *Creditor ID* - *Transaction Amount* - *Incoming Message Type*   The values of these fields can be changed or configured based on the client requirement.  If the duplicate check fails, the system routes the DD to repair or rejects it  Read [Repair](#Repair) or [Automated reject processing](#AutoRejProc) for more information. |
| Filtering | Filters payments when interfaced with a screening engine. This is a bank-specific requirement and is performed on site. During a hit from filtering, it routes the DD to repair.  Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Warehouse future dated | - Warehouses DD initiations or schedules for release on the calculated debit value date (which is equal to settlement date). - Validations (except bulk agreement and message format) are repeated on release. |
| Balance check | Checks if sufficient funds are available in the debtor’s account before posting an inward DD. If sufficient funds are not available, it performs the following:  - Cancels or rejects the DD transaction automatically - Routes to the Repair queue - Retries checking till the RCLD or settlement date. |
| Posting | Debits the debtor’s account with the transaction amount. If posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or rejects it. Read [Repair](#Repair) for more information. **Posting**   - Debit clearing suspense account is configured in PP.CLEARING.SETTING - Debit debtor is the client account   **Settlement Booking Entry**  If SEPA payments are settled on the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Repair | Routes the inward DD with validation errors to the Repair queue for user intervention or rejects it.  - The user can repair the DD or reject it (manually) from the Repair queue. - Automatic reject processing is available only for TPH, which can be enabled using the configuration in PP.CLEARING.SETTING. - Automatic reject processing is performed when the following are not available:   - Debit account   - Mandate   Read [Automated reject processing](#AutoRejProc) for more information. |
| Manual reject | Rejects the DD from the Repair queue (manually).  - To manually reject, go to **Admin Menu** > **Payment Hub** > **Local Clearing** > **Clearing Setting**, enter the reason code or description in *Error Information*, and submit the DD from the Repair.   - The system allows manual reject only when *CreateRejectMessageIndicator* is configured in PP.CLEARING.SETTING. - The DD is authorised based on the authorisation principle. - The transaction can be rejected, when the current business date is before the settlement date or on the settlement date before the clearing reject cut-off time. |
| Automated reject processing | Rejects DD automatically when the *AutomatedReturnIndicator* is set as Y.  Automated reject processing works on the condition that the current business date is before the settlement date or on the settlement date before the clearing reject cut-off time. |
| Original collection rejected | - Cancels DD and assigns status 998 (Rejected), when the system rejects an inward DD (automatically or manually). - Updates the total bulk amount to be settled with the clearing at the determined settlement date. |
| Generate and send pacs.002 message to clearing | Generates a pacs.002 reject message (or refusal message on behalf of the debtor) and sends it to clearing at the pre-defined clearing schedule. |

## Inward Processing of SEPA DD Reject Messages from Debtor Bank

This section describes the processing of a reject message initiated by the debtor’s bank.



The status report message (pacs.002) contains transaction information that is rejected or refused by a debtor for the corresponding original DD bulk (pacs.003) sent by a creditor bank.

| Activity | Description |
| --- | --- |
| Update status for the original outgoing DD bulk | - Updates the status of the original DD bulk sent by the creditor bank to PART (Partial) or RJCT (Reject), which indicates that an outgoing bulk has rejected transactions by the debtor bank. - To view the status of the bulk, go to **User Menu** > **Payments** > **Payments Hub** > **Payment Inquiries** > **Received and Sent File Details** > **Sent File Details**. |
| Update amount to be settled for the original outgoing DD bulk | - Updates the pending settlement transaction of the original outgoing DD bulk, which is executed on a clearing settlement day (after reject cut-off time). - Books the settlement transaction with the total amount of the collections in the original pacs.003 bulk sent, minus the total amount of rejected transactions in the bulk. |
| Reject the original outgoing DD | - Identifies and rejects the transactions based on the *Original Message ID* and *Original Transaction Reference* for each transaction in the pacs.002 message. - Generates a new reject transaction to refund the rejected amount if a rejected transaction is already booked (reject is received at the settlement date). |
| Original collection marked as Returned | Marks the status of the original (returned) collection as ‘Rejected’ (998), after rejecting the incoming DD return. |

Reject messages with certain ISO reason codes can be routed to a manual ‘Reject’ or Clearing Status Report queue (if configured), which is not considered in this module.

## Inward Processing of SEPA DD Return or Refund from Clearing

This section describes the processing of an incoming DD return from a SEPA clearing initiated by the debtor’s bank for the corresponding outgoing DD received from the creditor’s bank.



| Activity | Description |
| --- | --- |
| Message format validation | Validates pacs.004 message format by checking mandatory and non-mandatory fields, proper field length, and content based on pacs.004 XML definition language file provided by clearing. |
| Debit account validation | Validates if the debit account is a valid Temenos Transact account. If the account is invalid, frozen or closed, it routes the DD to repair. |
| Dates calculation | - Determines the credit value date as the inter-bank settlement date of the DD return (if pacs.003 bulk is available). If the inter-bank settlement date is a bank holiday, the credit value date is determined as the first banking business day (based on the cut-off shift day). - To configure one day in channel cut-off, go to **Admin Menu** > **Payment Hub**>**Routing and Settlement** > **Channel Cut-off Configuration**. - Based on the configuration, the debit value date is when the return payment is processed or equal to the *Original Interbank Settlement Date*. |
| Duplicate check | Enables to configure the checks based on the following:  - *End To End Reference* (customer-specific reference) - *RCLD* - *Mandate Reference* - *Creditor ID* - *Transaction Amount* - *Incoming Message Type*  If the check fails, the system routes DD to repair or rejects it. Read [Repair](#Repair) or [Automated reject processing](#AutoRejProc) for more information. |
| Identify original payment | Identifies the original outgoing payment transaction based on *Original Message ID* and *Original Transaction ID* in the incoming return or refund message. If the original transaction cannot be identified or fully processed, the system routes the return DD to the Repair queue. |
| Filtering | Filters payments when interfaced with a screening engine. This is a bank-specific requirement and is performed in the site. Upon getting a HIT from filtering, the system routes the DD to repair.  Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Balance check | Checks if sufficient funds are available in the debtor’s account before posting the debit return. If sufficient funds are not available, it performs the following:  - Routes the DD transaction to the Repair queue. - Retries checking till the settlement date. |
| Fees calculation | Charges interchange fees and compensation refund cost for the R-Message. These charges must be paid to the original debtor bank. In TPH, these charges are debited from the customer (original creditor). The payment fails posting (debit side is not equal to credit side), when these charges are not set up for the product as client charges. |
| Posting | Debits the debtor’s account with the transaction amount. If posting fails (due to a posting restriction), the system parks the payment in the Repair queue for user action or rejects it. Read [Repair](#Repair) for more information. **Posting**   - Debit clearing suspense account is configured in PP.CLEARING.SETTING - Debit debtor is the client account   **Settlement Booking Entry**  If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Original collection marked as ‘Returned’ | Marks the status of the original (returned) collection as Completed and Returned (996), when the incoming DD return is booked. |
| Repair | Routes the inward DD with validation errors to the Repair queue for manual intervention (repair). The system does not allow return or reject of an inward DD return. |

## Manual Return of Inward SEPA Payments

This section describes the manual return of incoming SEPA initiated by debtor's bank.



[Manual Return from the Repair Queue](#)

| Activity | Description |
| --- | --- |
| User initiates manual return or refund | Returns the DD from the Repair queue (manually), when:  - Inward SEPA direct debit cannot be booked on the settlement - Clearing cut-off time has already passed   - Direct debit is available or routed to the repair queue - Due to a posting restriction, closed or frozen account  Read [Inward Processing of SEPA DD from Clearing](#Inward_Processing_of_SEPA_DD_from_Clearing) for more information. |
| User enters reason code or description in the Error Information tab and submits | - Submits the DD from the Repair queue as ‘Returned’ with the reason code and description. - Indicates whether the return is originated on behalf of the bank or debtor in the **Error Information** tab. The submitted transaction must be approved by another user from the Authorisation queue. |
| Timeline validation (acceptance days for returns) | Checks for the maximum number of inter-bank business days allowed for a debtor bank to send a return transaction after the settlement date of the original collection.  - B2B DD – 3 days - CORE DD – 5 days   This is configured in PP.CLEARING.SETTING under *Acceptance Days for Returns* for the respective schemes. Read [Configuring SEPA Direct Debit](../Europe_SEPA_Direct_Debit_PPSPDD/Configuration.htm) for more infotmation.  - The system checks the timeline when the user submits the return from the Repair queue and sends a warning (if it exceeds). - The timeline is validated again when the user authorises the submitted return from the Repair queue. |
| Posting – inward SEPA DD | Debits the original amount of the incoming DD from a return suspense account (instead of the debtor’s account) and credits the clearing suspense account, when:  - The user submits the DD from the Repair queue as ‘Returned’ - Another user approves the submitted transaction |
| Creates new DD return | A new SEPA DD return is created when the inward DD is booked. |
| Posting – DD return | A new SEPA DD return is created with the following posting:  - Credit return suspense account is configured in PP.CLEARING.SETTING - Debit clearing’s suspense account is configured in PP.CLEARING.SETTING   **Settlement Booking Entry**  If SEPA returns are settled at the clearing settlement date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. This happens when the return file is sent to the clearing as the returns are pre-settled. |
| Original collection marked as Returned | Marks the status of the original (incoming and returned) collection as Completed and Returned (996) if an outgoing DD return is booked. |
| Generate pacs.004 message | Generates a pacs.004 return message (or Refund message when it is returned on behalf of the debtor) and sends it to clearing at the pre-defined clearing schedule. |

[Manual Return, Refund from the Return or Refund Page](#)

| Activity | Description |
| --- | --- |
| User initiates manual return or refund | The Operator can manually refund the original direct debit, when:  - Inward SEPA DD is already booked on the settlement date. - Debtor requests the debtor bank to refund its account with the original collection amount.  To initiate manual return or refund, go to **User Menu** > **Payments** > **Payments Hub** > **Payment Investigations and Cancellations** > **Return/Reject Payments** > **Return/Reject Inward Direct Debits**. |
| System creates new DD return in OE page | Creates a DD return or refund transaction (for which the reason code and description can be entered) if the user selects and confirms to return or refund the original outgoing DD. |
| User enters reason code or description in the Error Information tab and submit | - Submits the DD from the Repair queue as Returned with the reason code and description. - Indicates if the return originates on behalf of the bank or debtor (return or refund) in the **Error Information** tab.   The submitted transaction must be approved by another user from the Authorisation queue. |
| Timeline validation (Acceptance days for returns) | - Checks the maximum number of inter-bank business days a debtor bank is allowed to send a return transaction, after the settlement date of the original collection.   - B2B DD – 3 days   - CORE DD – 5 days   - Refunds (only CORE scheme):     - Authorised mandate - 8 weeks + 2 inter-bank business days     - Unauthorised mandate - 13 months - The number of days is configured in PP.CLEARING.SETTING.   Read [Configuring SEPA Direct Debit](../Europe_SEPA_Direct_Debit_PPSPDD/Configuration.htm) for more information.. - Checks the timeline when the user submits the return from the Repair queue and sends a warning (if the timeline exceeds). - Validates the timeline again when the user authorises the submitted return from the Repair queue. |
| Posting – inward SEPA DD | Applies the following postings if a user submits the DD from the Return entry page as Returned, and another user approves and submits that the return is valid (time line):  - Credit return suspense account is configured in PP.CLEARING.SETTING. - Debit clearing’s suspense account is configured in PP.CLEARING.SETTING.   **Settlement Booking Entry**  If SEPA returns are settled at the clearing settlement date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account.  Debits the original amount of the incoming DD from a return suspense account (instead of the debtor’s account) and credits the clearing suspense account. |
| Posting –  DD return | Creates a new SEPA DD return with following posting:  - Credit original debtor’s account. - Debit clearing’s suspense account is configured in PP.CLEARING.SETTING.   **Settlement Booking Entry**  If SEPA returns are settled at the clearing settlement date, the system checks and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Original collection marked as Returned | Marks the original (incoming and returned) collection status as Completed and Returned (996) if an outgoing DD return is booked. |
| Generate pacs.004 message | Generates a pacs.004 return or refund message (if returned on behalf of the debtor) and sends it to clearing at the pre-defined clearing schedule. |

A pacs.004 return message is sent to the respective SEPA clearing, when returns are initiated from the **Manual Repair** page, or returned or refunded from the **Return or Refund** page. Similar to outgoing DD, the system performs reachability checks, EPC common validations, and clearing-specific validations (if configured).

In this topic

- [Introduction to EPC SEPA Direct Debit](#IntroductiontoEPCSEPADirectDebit)

- [Types of Payment and Messages](#TypesofPaymentandMessages)
- [Processing Post and Pre-Settlement DD](#ProcessingPostandPreSettlementDD)
- [SEPA DD Schemes](#SEPADDSchemes)
- [Processing DD Batches and Single DD](#ProcessingDDBatchesandSingleDD)
- [Processing Recurrent and One-Off DD](#ProcessingRecurrentandOneOffDD)
- [Validating SDD Mandate](#ValidatingSDDMandate)
- [SEPA Direct Debit R-Transactions](#SEPADirectDebitRTransactions)
- [Pre-Settlement SDD Events or Messages](#PreSettlementSDDEventsorMessages)
- [Post-Settlement SDD Events or Messages](#PostSettlementSDDEventsorMessages)
- [Bulking Criteria](#BulkingCriteria)
- [Outward Processing of DD Initiation](#OutwardProcessingofDDInitiation)
- [Book Processing of DD Initiation](#BookProcessingofDDInitiation)
- [Inward Processing of SEPA DD from Clearing](#InwardProcessingofSEPADDfromClearing)
- [Inward Processing of SEPA DD Reject Messages from Debtor Bank](#InwardProcessingofSEPADDRejectMessagesfromDebtorBank)
- [Inward Processing of SEPA DD Return or Refund from Clearing](#InwardProcessingofSEPADDReturnorRefundfromClearing)
- [Manual Return of Inward SEPA Payments](#ManualReturnofInwardSEPAPayments)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:19:57 PM IST