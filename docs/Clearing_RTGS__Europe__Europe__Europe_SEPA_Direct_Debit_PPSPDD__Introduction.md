# Introduction to SEPA Direct Debit

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_SEPA_Direct_Debit_PPSPDD/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [SEPA Direct Debit](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
  - [Swiss Interbank Clearing Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
  - [SEPA Instant Clearing-EBA INST SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
  - [SEPA Credit Transfer SEPA Credit Transfer](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Introduction.htm)
  - [SEPA Direct Debit SEPA Direct Debit](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Introduction.htm)
    - [Introduction](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Introduction.htm)
    - [Configuration](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Configuration.htm)
    - [Working with](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Working_with.htm)
    - [Tasks](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Tasks.htm)
    - [Outputs](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Outputs.htm)
  - [TARGET2 Clearing TARGET2 Clearing](../../Europe/Europe_Target2_PPTGTC/Introduction.htm)
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

# Introduction to SEPA Direct Debit

Updated On 10 July 2025 |
 68 Min(s) read

Feedback
Summarize

Single Euro Payments Area (SEPA) initiative was created to support Electronic Euro payments. It make it easy and convenient for citizen and business to pay across Europe with one payment account and card from their home countries. The European Payment Council (EPC) has created the implementation standards and rule books for SEPA. It has four Euro payment schemes:

- Credit transfer
- Direct debits (DD) core scheme
- DD business-to-business scheme
- Instant credit transfer

The area in which these payment schemes (for all euro credit transfers and DD) are available is broader than the European Union. It covers 36 countries and territories, such as 28 Member States plus Iceland, Norway, Liechtenstein, Switzerland, Monaco, San Marino, Andorra and Vatican City State or Holy See. The following sections describes the usage and configuration of SEPA CORE and Business-to-Business (B2B) DD scheme transactions:

- SEPA Direct Debit (STEP2) module in Temenos Payments Hub is compliant to ‘EBA STEP2 – Multi Purpose Direct Debits Core Service and B2B Service - 2025’
- To know more about DD and its uses, refer to [Direct Debits](../../Payments_Hub_(PP)/Direct_Debits/Introduction.htm#top).

## Business Events, Transaction Types, and Message Types

SEPA Direct Debits (SDD) scheme bulks and processes the messages as files. TPH supports the following files and messages types.

| File Type | Name | Description |
| --- | --- | --- |
| IDF | Input Debit File | The direct participant’s systems use this file to transmit transactions to the central system. |
| DVF | Debit Validation File | Indicates the success or otherwise of the validation process. The central system returns this file, per transmitted IDF, to the sending direct participant. |
| DNF | Debit Notification File | Notifies the relevant counterparty on the accepted Direct Debits transactions, pre-settlement and post-settlement R-messages. |
| RSF | Results of Settlement File | It includes the status of DD collections and the post-settlement R-messages, which have been sent to the settlement system for the relevant business date. It is delivered to the relevant direct participants, at the end of the settlement phase in a window specified during the daily cycle. Each direct participant receives a single RSF notifying them of all the DD collections and post-settlement R-messages for which they are either the Instructed or Instructing Agent (either debtor or creditor DPs). |
| LNR | Liquidity Notification Report | STEP2-CGS notifies the direct participants whenever there is threshold exceeded in its liquidity position or when liquidity adjustment is executed. |

TPH supports the following SEPA DD message types:

| Business Event | Transaction Type | Description | ISO Message | Version |
| --- | --- | --- | --- | --- |
| DD transfer initiation | DD | - Receives and executes Customer-to-Bank DD collection requests. - Validates the request received from the creditor and routes it through appropriate clearing (when the debtor belongs to another bank), based on the Requested Collection Date (RCLD), cut-off time, and days required for the clearing to finally settle the amount. - Warehouses the payments with a future value date and processes on the due date. - Forwards the finalised payment to clearing in pacs.003 message format or other supported native clearing format. - Raises settlement entries at the RCLD or settlement date. | pain.008 or initiated through `PP.ORDER.ENTRY` (OE) DD book or outgoing page | 02 and 08 |
| DD | DD | - Receives and processes Bank-to-Bank DD payment orders to debit the debtor in the books of the processing bank. - Executes DD successfully, when it:   - Supports debit instruction with appropriate mandates   - Has sufficient funds in the debtor account - Otherwise, the debit item is rejected or returned. | pacs.003 | 08 |
| DD reject | RJ | - A negative confirmation of direct debit item received by the debtor bank. - TPH performs the following:   - Send an outbound DD rejection message (pacs.002), when DD instruction from clearing cannot be processed successfully (for example, the debtor mandate is not available and funds are insufficient in the debtor account).   - Allow the transformation of rejection messages in non-ISO format to support native clearing formats.   - Receive inbound DD reject message (pacs.002) and mark the previously sent collection item as Rejected (which are excluded for Settlement). | pacs.002 | 10 |
| Return debit transfer or DD | RF | - Enables the return of DD after the settlement date, when it is within the allowed time period of the clearing. It is initiated by the debtor bank. - TPH performs the following:   - Supports automated and manual return of incoming DD that are unsuccessful.   - Generates pacs.004 or other native clearing message format for supported outgoing returns clearing.   - Supports DD returns received by the creditor bank for previously originated debits.   - Receives the returns as pacs.004 messages and process them as STP.   - Supports native clearing formats for DD returns as a feature of the relevant clearing. | pacs.004 | 09 |
| Debit refunds | RD | - DD can be returned manually at the request of the debtor, within the allowed time period when supported by the clearing. - TPH perform the following:   - Generates pacs.004 message for outgoing DD refunds.   - Supports native clearing formats for DD refund in the respective Clearings.   - Supports receipt of DD refunds from debtor bank by using clearing and processes them by debiting the creditor who initiated the DD. | pacs.004 | 09 |
| Customer payment (DD) reversal | RV | - Creditor Bank can receive a payment (DD) reversal request (pain.007 message) from the creditor. - TPH can perform the following:   - Support the receipt of customer payment reversal message (pain.007) to reverse a previously initiated DD.   - Reversals accepted are processed STP by debiting the creditor (initiating the reversal) and crediting the beneficiary.   - Generates an outgoing pacs.007 message for DD reversals to clearing.   - Supports the native clearing formats in the relevant clearing feature. | pain.007 or initiate a reversal of a processed DD through OE | 02 and 09 |
| DD reversal | RV | - Debtor bank can receive an incoming DD reversal from the creditor bank through the clearing. - TPH can receive DD reversals (pacs.007) and credit the debtor account. | pacs.007 | 09 |
| Liquidity Notification Advice | LNR | - STEP2-CGS can send Liquidity Notification Report (LNR) to the Continuous Gross Settlement’s (CGS) preferred agent BIC to notify the balance or the position update on the receiving bank’s accounts held with STEP2-CGS. - LNR represents a credit advice or a debit advice if the accounts of the participating banks is credited or debited in the Account Holding Institution (AHI) due to liquidity transfer operations between the accounts. | camt.054 | 06 |

## Post and Pre-Settled

Temenos Payments Hub supports the processing of,

- Pre-Settled Direct Debit (for example, BACS) instructions – Settlement transaction is created during message generation.
- Post-Settled Direct Debit (for example, SEPA DD) instructions – Settlement transaction is generated on the requested collection date.

This section helps the user to understand the post and pre-settlement.

[Pre-Settlement](#)

SEPA DD is initiated and sent to clearing pre-settlement (one interbank business day and maximum 14 days before the request collection or settlement date). It is booked or settled on the request collection or settlement date. Settlement booking entries to the clearing Nostro account occur on the settlement date (RCLD) for the total amount of DD (each DD bulk sent to the clearing) considering all the rejections till the settlement date. DD can be cancelled by the creditor’s bank or rejected by the debtor’s bank (or refused by the debtor through debtor bank) pre-settlement (before the clearing reject cut-off).

[Post-Settlement](#)

After clearing settlement, DD (processed or completed and settled by the clearing) can be reversed by initiating DD reversal by the creditor bank, returned by the debtor bank or refunded by the debtor (through debtor’s bank). The debtor can initiate the timeline (period) within a refund depending on the authorisation or unauthorisation of DD mandate.

## SEPA DD Schemes

The following are the two types of schemes in SEPA DD:

| Scheme | User | Description |
| --- | --- | --- |
| SEPA Direct Debit B2B | Business (B2B) | SDD B2B payments are usually between businesses (but the creditor can be an individual customer). PSP participation is optional. Debtor PSP should maintain the mandate and check validity while processing collection requests according to the SDD rule book by EPC. Hence, the refund option is not available for the debtor after SDD is processed successfully. |
| SDD CORE | Consumer (CORE) | SDD Core payments are between customers and businesses. PSP participation is mandatory. Debtor banks must check the mandates as an additional or optional service while processing collection requests. A refund option is available for the debtor even after SDD is processed successfully. |

To choose the DD scheme, the user needs to provide the Local Instrument Code as CORE or B2B.

Both the schemes operate in Euro.

The following can be different for each scheme:

- Timelines in which SDD business events occur
- Configuration of timelines and mandate verification (by debtor bank)

To know more, refer to [Pre-Settlement and Post-Settlement SDD](#Post_and_Pre-settled) events.

## DD Batches versus Single DD

TPH system supports DD batch and single DD processing.

[DD Batch](#)

DD in one batch is initiated and bulked in a pain.008 message bulk (the *Batch Booking* or *Indicator* is set as True). If it is not available in the pain.008 message, the *Batch Booking* field is set as True (as part of a Netting agreement configured for the submitter of the bulk or default Netting agreement). A pain.008 file has multiple DD batches (bulks) with different *RCLD*. The system processes the DD batch as follows:

- One (parent) transaction for crediting the creditor’s account and debiting a batch suspense (wash) account with the total amount of DD in the message bulk.
- Child transaction for each DD (child) in the batch, debiting the debtor’s account (in book transaction) or clearing suspense account (outgoing transaction) and crediting the batch suspense (wash) account with the individual DD amount.

[Single DD](#)

Single DD is initiated and bulked in a pain.008 message bulk for which the *Batch Booking* field is set as False. If it is not available in the pain.008 message, the *Batch Booking* field needs to be configured as False (as part of a Netting agreement). The system creates a single transaction for each DD in the batch, debiting the debtor’s account (for book transaction) or clearing suspense account (outgoing transaction) and crediting the creditor’s (client) account with the individual DD amount.

## Recurrent and One-Off DD

The scheme caters to both recurrent and one-off collections based on the Mandate Type and Sequence Type (RCUR or OOFF) in the DD.

| Type | Description |
| --- | --- |
| Recurrent DD | Debtor’s authorisation is used for regular DD initiated by the creditor |
| One-off DD | Debtor’s authorisation is given only once to collect one single DD. This cannot be used for any subsequent transaction. |

The system supports validation of both the DD. To know more, refer to [SDD Mandate Validation](#SDD_Mandate_Validation).

## SDD Mandate Validation

The system validates a mandate in the DD management system (provided in an incoming DD collection as a debtor bank), when configured in the clearing setting for the respective DD scheme (CORE or B2B). To know more, refer to the following sections in Direct Debits: [Mandate Validation and Auto-registration of Mandate](../../Payments_Hub_(PP)/Direct_Debits/Introduction.htm#Mandate_Validation_and_Auto-registration_of_Mandate), [Mandate Limit Check, and Creditor Restrictions](../../Payments_Hub_(PP)/Direct_Debits/Introduction.htm#Mandate_Limit_Check_and_Creditor_Restrictions). The following attributes of the mandate available in an incoming SEPA DD message are compared to the mandate in the mandate administration (DD.DDI):

- *Identification Code of the Scheme* (B2B or CORE)
- *Unique Mandate Reference*
- *Identifier of the Creditor* (*Creditor ID*)
- *Account Number of the Debtor (IBAN)*
- *BIC Code of* *Debtor Bank*
- *Transaction Type*

All the attributes in the list needs to be identical, except *Transaction Type*.

If recurrent collection is available for one-off mandate, then it does not cover the successive collections available after the first collection. In addition to the above attributes, the following factors are checked for each mandate of a SEPA DD collection:

- Mandate is not cancelled by the Debtor or Creditor
- Not exceed maximum number of transactions setup for the mandate
- Amount of the collection cannot exceed the maximum amount setup for the mandate
- Periodicity setup for the mandate in the mandate administration (available only on certain days of the month or week)

## SEPA Direct Debit R-Transactions

Participant PSPs must manage exceptions that arise when one of the parties involved in direct debit transaction is unable to process a collection request. In such cases, the PSP must initiate (and should have the ability to receive) rejects, returns, refunds and reversals (collectively called as R-transactions).

The type of R-transaction used depends on the initiator or message and point at which the R-transaction is initiated or sent. The below diagram explains the type of R-message based on time and party of initiation.



Temenos allows the participant PSPs to manage the above messages.

According to the SDD scheme guidelines, participants must channel rejects, returns and refunds of SDD collections through the same CSM used for the clearing and settlement of the original SDD collection, unless otherwise agreed between the SDD scheme participants.

## Pre-Settlement SDD Events or Messages

The below table portrays SEPA DD events or messages before clearing settlement, as a set of steps and events in the order of occurrence. It includes all the rejects, refusals or cancellation requests of a DD transaction (Pre-settlement R-messages).

| Business Event or Timeline | Creditor | <--> | Creditor Bank | <--> | Clearing Settlement at Settlement Date (D) | <--> | Debtor Bank | Debtor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD initiated: <*RCLD-14C* | Initiate DD | --> pain.008 | Warehouses and releases at RCLD-14C | --> pacs.003 | Scheduled at *D*=RCLD | --> pacs.003 | Receives at D-14 | Option for refusal |
| DD initiated: > RCLD-14C and <= RCLD-1TD | Initiate DD | --> pain.008 | Validates and sends the message to clearing on the same day. DD scheduled at due date or book date = RCLD | --> pacs.003 | *D*=RCLD | --> pacs.003 | Receives on the same day, the creditor initiates the DD | Option for refusal |
| DD initiated: *RCLD* | Initiate DD | --> pain.008 | Validates and sends the message to clearing on the same day. DD scheduled at due date = RCLD+1C | --> pacs.003 (with *RCLD* = *RCLD+1C*) | *D* = RCLD+1 | --> pacs.003 | Receives on the same day, the creditor initiates the DD | Option for refusal |
| DD refused by debtor: <= *D* before reject cut-off |  | <-- pain.002 (optional based on configuration) | Rejects DD transaction. Do not settle register transaction at D | <--pacs.002 | Do not settle register transaction at *D* | <--pacs.002 | Refusal message initiated on behalf of the debtor | Request for refusal to the bank |
| DD reject by debtor bank: <=*D* before reject-cutoff |  | <-- pain.002 (optional based on configuration) | Rejects DD transaction. Do not settle register transaction at *D* | <--pacs.002 | Do not settle register transaction at *D* | <--pacs.002 | Rejects message initiated on behalf of the debtor bank |  |
| DD cancellation request by creditor bank:  <= *D* before reject-cutoff |  |  | Initiates cancellation request on behalf of creditor or bank | --> camt.056 | Do not settle register transaction at *D* | --> camt.056 | Rejects DD transaction. Do not settle register transaction at *D* |  |
| Settlement at D | Creditor account debited (\*) |  | Books clearing settlement transaction (\*\*) |  | Settled at *D* or *D+1TD* (when *D* is not a banking business day) |  | Clearing settlement transaction booked (\*\*) | Debtor account debited (\*) |

The description of the values given in the above table is as follows:

| Value | Description |
| --- | --- |
| *RCLD* | Requested collection date available in a pain.008 DD transaction |
| *C* | Calendar days (for example, 14C = 14 calendar days) |
| *D* | Clearing settlement date of the pain.008 bulk |
| *TD* | Interbank business days (TARGET days) |
| *DD* | Direct debit |

- A DD transaction booked at *D* cannot be rejected by debtor bank, refused by debtor or cancelled through cancellation request by creditor bank.
- If *D* is a local bank holiday, the debtor is debited at *D* + 1 banking business day.

The clearing settlement transaction is booked at *D* as follows:

| Type of Bank | Account | Note |
| --- | --- | --- |
| Creditor bank | - Debit – Clearing account (Nostro) - Credit – Clearing suspense account | Total requested settlement amount of the outgoing pacs.003 bulk is subtracted with any cancelled DD transactions (by a cancellation request). |
| Debtor bank | - Debit – Clearing suspense account - Credit – Clearing account (Nostro) | Total requested settlement amount of an incoming pacs.003 bulk is subtracted with any rejected DD transactions (by the debtor bank or on behalf of a refusal from the debtor). |

## Post-Settlement SDD Events or Messages

The below table displays the post-settlement events or messages as a set of steps that occurs after clearing settlement of the DD. The timeline mentioned for each business event, in which the event can differ for CORE and B2B DD.

| Business Event or Timeline | Creditor | <--> | Creditor Bank |  | Clearing Settlement | <--> | Debtor Bank | Debtor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD return by Debtor bank (\*):  - For CORE: <= *D*+*5TD* - For B2B: <= *D*+*3TD* | Debited with original amount of original DD transaction |  | Books clearing settlement transaction (\*\*) | <--pacs.004 | Receives the forward return that is settled on the date return. This is the interbank settlement date in pacs.004 | <--pacs.004 | Initiates return message and sends it to clearing. Books clearing settlement transaction (\*\*) | Credits debtor account with original amount of original DD transaction returned |
| DD refund by debtor for authorised debit mandate:  - For CORE:<= *D*+ 8 weeks - For B2B: No refund option | Debited with original amount of original DD transaction |  | Books clearing settlement transaction (\*\*) | <--pacs.004 | Receives the forward return that is settled on the date return. This the interbank settlement date in pacs.004 | <--pacs.004 | Initiates return message and sends it to clearing. Books clearing settlement transaction (\*\*) | Credits debtor account with original amount of original DD transaction returned |
| DD reversal by creditor: <= *D*+*5**TD* | Debited with the amount of the reversal of a settled collection | -->pain.007 | Validates and sends reversal to clearing, on the date it receives the reversal. Books clearing settlement transaction (\*\*) | -->pacs.007 | Receives the forward reversal that is settled on the date reversal | -->pacs.007 | Credits debtor account with the amount of the reversal. Books clearing settlement transaction (\*\*) | Credits debtor account with the amount of the reversal of a settled collection. Book date or credit value date is configurable (no limitation by the scheme) |

The description of the values given in the above table is as follows:

- *D* – Clearing settlement date of the pacs.003 bulk
- *TD* – Interbank business days (TARGET days)

| Date for Settlement | Scheme | Day |
| --- | --- | --- |
| Return | CORE | 5 interbank business days (after the settlement date of the collection available to the debtor bank) |
| Business-to-Business (B2B) scheme | 3 days |
| Refund | CORE | 8 weeks +2TD interbank business days (after the settlement date of the collection available to the debtor bank) |
| B2B | Not allowed or supported in the scheme |

The system checks the timeline for incoming DD return or refund, and routes the transaction to the Repair queue (if timeline is exceeded).

| Type of Bank | Refund | Reversal |
| --- | --- | --- |
| Creditor Bank | A clearing settlement transaction is booked as follows for return or refund messages:  - Debit – Clearing suspense account - Credit – Clearing account (Nostro)   Total requested settlement amount of the incoming pacs.004 bulk. | A clearing settlement transaction is booked as follows for reversal messages:  - Debit – Clearing suspense account - Credit – Clearing account (Nostro)   Total requested settlement amount of the outgoing pacs.007 bulk. |
| Debtor Bank | A clearing settlement transaction is booked as follows for return or refund messages:  - Debit – Clearing account (Nostro) - Credit – Clearing suspense account   Total requested settlement amount of the outgoing pacs.004 bulk. | A clearing settlement transaction is booked as follows for reversal messages:  - Debit – Clearing account (Nostro) - Credit – Clearing suspense account   Total requested settlement amount of the incoming pacs.007 bulk. |

## Bulking Criteria

The outgoing SEPA DD files sent to the clearing can be bulked with different message types (CORE and B2B DD) in separate outgoing input DD files (IDFs). The outgoing file can have multiple bulks with multiple transactions, and can have pacs.008, pacs.004, pacs.007, pacs.002 and camt.056 bulked in one file. Different message types cannot be bulked in one bulk (for example, pacs.008 and pacs.004 cannot be bulked in the same bulk but as two separate bulks in the same file). The transactions are grouped in a message bulk based on the following bulking criteria:

| Message | Description |
| --- | --- |
| pacs.003 | *RCLD* (= calculated debit value date of the DD) |
| pacs.004 | Interbank settlement date (= calculated debit value date of the DD return) |
| pacs.007 | Processing date (= credit value date of the DD reversals) |
| pacs.002 | Processing date (= date of the reject or refusal) |
| camt.056 | Processing date (= date when cancellation request has been initiated) |

## Outward Processing of DD Initiation

This section describes the outward processing of a DD order initiated in TPH or ordering bank.



| Activity | Description |
| --- | --- |
| Manual capture of SEPA DD initiation from branch or back office by using OE page | - Captures a SEPA DD from TPH OE page. - Validates (mandatory and non-mandatory) fields and inputs data on submission. |
| Outgoing DD payment instructions through ordering bank | Sends DD payment instructions to TPH bank through ordering party’s bank (same as TPH bank or another bank). The instruction is in the pain.008.001.02 or pain.008.001.08 – ISO20022 format. |
| File duplicate check | Checks whether a file is received from a channel other than TPH OE. If a duplicate file is found, it rejects and sends a negative pain.002 message to the initiating bank or system (if configured). This check is based on the following combination of fields in the pain.008 file:  - Group header message identification - Message format of the file - Group header initiating party organisation IDBIC - Source from which the pain.008 file is originated |
| Format validation | Validates the pain.008 message format by checking mandatory and non-mandatory fields, proper field length, and content based on pain.008.001.02 XML definition language. |
| Bulk agreement validation | - Validates pain.008 bulks against a netting agreement setup for the submitter of the bulk. - To perform this, go to **Admin Menu** > **Payment Hub** > **Debit Authority** > **Netting Agreements**.   - Netting agreement validation can be skipped when the *Message* *Type* (pain.008) is configured in the No DA List (in the Debit Authority menu). - Bulk agreement validation is not applied for DD initiated from TPH OE page.  To know more, refer to Bulk or Netting Agreement. |
| Credit account validation | Validates the following for the ordering account:  - Is a valid Temenos Transact Account - Has a posting restriction |
| Execution warehouse | Warehouses DD initiations that are received 14 calendar days (or more) prior to the RCLD (which is configured in *Max Allowed Days* in Source settings) or scheduled for release on RCLD minus 14 calendar days. The following is performed in a DD batch that is received 14 calendar days (or more) before RCLD:  - Warehouses the parent (total amount) transaction - Creates child transactions from the batch when the parent transaction is released and validates it successfully |
| Determine SEPA outgoing clearing | - Determines the outgoing clearing channel from the RS Channel Selection List. - To access this, go to **Admin Menu** > **Payment Hub** > **Routing and Settlement**. - The clearing suspense account is determined for the respective outgoing SEPA clearing channel (for example, STEP2). |
| Reachability check | Validates whether the debtor bank (BIC) is reachable through the selected SEPA clearing. To know more, refer to [Reachability](../../Payment_Initiation_(PI)/Reachability/Introduction.htm). |
| SEPA channel validations | Performs this validation on the DD to ensure that it meets the compliance requirements of the SEPA clearing. The following fields are validated or need to be mandatory:  - *Local Instrument Code* - *Sequence Type* - *Transaction Amount* - *Transaction Currency Code* (needs to be equal to EUR) - *Details of Charges* (needs to be equal to SHA or SLEV) - *RCLD* - *Mandate Identification* - *Mandate Date Of Signature* - *Creditor ID* - *Creditor Name* - *Creditor Account* (a valid IBAN) - *Creditor ID* - *Debtor Name* - *Debtor Account* (a valid IBAN) - *Debtor Agent BIC* (available or system-driven) |
| Dates calculation | Calculates the DD (debit and credit) value dates and booking date. Basics rules for date calculation for outgoing transactions are as follows:  - If the *RCLD* of the DD initiation is equal to or before the current business date, the collection or settlement date is set one banking business date ahead from the current business date (based on the configured settlement shift for the respective SEPA clearing, which is 1 day for both CORE and B2B scheme DD). - If the clearing cut-off time has already passed when applying the settlement shift, the system applies another cut-off shift day (1 day).   To configure the settlement and cut-off shifts, go to **Admin Menu** > **Payment Hub** > **Routing and Settlement** > **Channel Cut-off Configuration**.  Calculates the debit and credit value dates and book date, which is equal to determined collection or settlement date. |
| Duplicate check | Enables to configures the check based on the following criteria: DD batch booking (parent transaction that books the total amount)  - *Account of the Credit Party* - *Currency of the Credit Account* - *Transaction Amount* - *Currency* - *RCLD* - *Bulk Reference*  Each DD transaction in a batch  - *Account of the Debit Party* - *Currency of the Debit Account* - *Transaction Amount* - *Transaction Currency* - *RCLD* - *Instruction Identification*  Single outgoing DD transaction (batch booking is false)  - *Account of the Credit Party* - *Currency of the Credit Account* - *Transaction Amount* - *Transaction Currency* - *RCLD* - *Instruction Identification*   The system can configure and change (if required) the duplicate checks. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Generate and send pacs.003 to clearing | Bulks DD initiations and sends a pacs.003 message to the respective SEPA clearing, when:  - DD transactions are received at least 14 days prior the given *RCLD* - All business validations are qualified |
| Warehouse future dated | Warehouses DD initiations or schedules for release on the calculated debit value date (which is equal to settlement or collection date). |
| Fees calculation | Charges creditor for any fees. Fees for child DD transactions are booked or posted (similar to single DD transactions and not along with batch parent transaction). |
| Posting | Credits the creditor’s account with the transaction amount.  If the posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or is cancelled. To know more, refer to Error Queue section. **Posting**   - If a DD initiation is a child of a batch (booking indicator is true or configured as a part of the netting agreement), then:   - Debit clearing suspense account is configured in Clearing setting   - Credit batch suspense account is configured for each company - If a DD initiation is a single transaction (booking indicator is false or configured as a part of the netting agreement), then:   - Debit clearing suspense account is configured in Clearing setting   - Credit creditor is the ordering client - Total requested bulk amount of a batch booking transaction is known as the parent transaction of the batch children, in which:   - Batch suspense account is configured for each company   - Credit creditor is the ordering client   **Settlement Booking Entry**   - If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Error queue | Rejects batch child transactions with validation errors by performing the following posting on the settlement or collection date:  - Debit creditor is the ordering client - Credit batch suspense account is configured for each company  Routes single or parent transaction (parent books the total amount of the batch) with validation errors to the Repair queue for user intervention or is cancelled automatically. - Automatic cancellation is available only for TPH. - Additionally, it routes invalid batch children to the Repair queue (similar to single DD that is based on specific configuration as part of a Netting Agreement, the *Repair**BatchChild* field is set as Y). |

## Book Processing of DD Initiation

This section describes the processing of a DD book order initiated in TPH or ordering bank.



| Activity | Description |
| --- | --- |
| Manual capture of SEPA DD initiation from branch or back office by using OE page | - Captures a SEPA DD from TPH OE page. - Validates mandatory and non-mandatory fields and inputs the data on submission. |
| Outgoing DD payment instructions through ordering bank | Sends DD payment instructions to TPH bank through ordering party’s bank (same as TPH or another bank). The instruction is in pain.008.001.02 or pain.008.001.08 – ISO20022 format. |
| File duplicate check | Checks whether a file is received from a channel other than `PAYMENT ORDER` (`PO`) application or TPH OE. Rejects the file (if it is a duplicate) and sends a negative pain.002 message to the initiating bank or system (if configured). This check is based on the following combination of fields in the pain.008 file:  - Group header message identification - Message format of the file - Group header initiating party organisation Id BIC - Source from which the pain.008 file is originated |
| Format validation | Validates the pain.008 message format by checking mandatory and non-mandatory fields, proper field length and content based on pain.008.001.02 XML definition language. |
| Bulk agreement validation | - Validates pain.008 bulks against a netting agreement setup for the submitter of the bulk. - To perform this, go to **Admin Menu** > **Payment Hub** > **Debit Authority** > **Netting Agreements**.   - Netting agreement validation can be skipped when the *Message Type* (pain.008) is configured in the No DA List (in the **Debit Authority** menu). - Bulk agreement validation is not applied for DD initiated from TPH OE page.  To know more, refer to Bulk or Netting Agreement. |
| Credit account validation | Validates the following for the ordering account:  - Is a valid Temenos Transact Account - Has a posting restriction |
| Execution warehouse | Warehouses DD initiations that are received 14 calendar days (or more) prior to the *RCLD* (which is configured in *Max Allowed Days* in Source settings) or scheduled for release on RCLD minus 14 calendar days. The following is performed in a DD batch that is received 14 calendar days (or more) before RCLD:  - Warehouses the parent (total amount) transaction - Creates child transactions from the batch when the parent transaction is released and validates it successfully |
| Debit account validation | Validates the following for the debtor account:  - Is as valid Temenos Transact Account - Has a posting restriction |
| Dates calculation | Calculates the DD (debit and credit) value dates and booking date.  - If the *RCLD* of the DD initiation is equal to or before the current business date, the collection or settlement date is set one banking business date ahead from the current business date (based on the configured settlement shift for the respective LEDGER, which is 1 day for both CORE and B2B scheme DD). - If the clearing cut-off time has passed when applying the settlement shift, the system applies another cut-off shift day (1 day).   To configure the settlement shift and cut-off shift, go to **Admin Menu** > **Payment Hub** > **Routing and Settlement** > **Channel Cutoff Configuration**.  Calculates the debit and credit value dates and book date, which equals the determined collection or settlement date. |
| Duplicate check | Enables to configure the check based on the following criteria: DD batch booking (parent transaction that books the total amount)   - *Account of the Credit Party* - *Currency of the Credit Account* - *Transaction Amount* - *Currency* - *RCLD* - *Bulk Reference*   Each DD transaction in a batch   - *Account of the Debit Party* - *Currency of the Debit Account* - *Transaction Amount* - *Transaction Currency* - *RCLD* - *Transaction Identification*   Single book DD transaction (batch booking is false in the DD)   - *Account of the Credit Party* - *Currency of the Credit Account* - *Account of the Debit Party* - *Currency of the Debit Account* - *Transaction Amount* - *Transaction Currency* - *RCLD* - *Transaction Identification*   The system can configure and change the duplicate checks. |
| Warehouse future dated | Warehouses DD initiations or schedules release on the calculated debit value date (which is equal to settlement or collection date). |
| Fees calculation | Charges creditor and debtor for any fees (if configured). Fees for child DD transactions are booked or posted (similar to single DD transactions and are not posted along with the batch parent transaction). |
| Balance check | Checks whether sufficient funds are available in the debtor’s account before posting a DD transaction (child of a batch or single DD).  - If sufficient funds are not available, it performs the following:   - Cancels or rejects the DD transaction (automatically)   - Routes to the Repair queue   - System can retry checking till the *RCLD* or settlement date. The system can be configured to retry debiting the debtor’s account even a few days after the settlement date (based on *Settlement* *Retry Days* configured as part of a netting agreement). - If sufficient funds are not available in the debtor’s account on the settlement date and any configurable settlement retry days, the system rejects the DD. |
| Posting | Credits the creditor’s account with the transaction amount. If posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or is cancelled. To know more, refer to Error Queue. **Posting**   - If a DD initiation is a child of a batch (batch booking indicator is true or configured as a part of the netting agreement), then:   - Debit clearing suspense account is configured in Clearing Setting   - Credit batch suspense account is configured for each company) - If a DD initiation is a single transaction (batch booking indicator is false or configured as a part of the Netting Agreement), then:   - Debit clearing suspense account is configured in Clearing setting)   - Credit creditor is the ordering client - Total requested bulk amount of a batch booking transaction is known as the parent transaction of the batch children, in which:   - Batch suspense account is configured for each company)   - Credit creditor is the ordering client   **Settlement Booking Entry**  If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Error queue | Rejects batch book child transactions with validation errors by performing the following posting on the settlement or collection date:  - Debit creditor is the ordering client) - Credit batch suspense account is configured for each company)   Routes single transactions or DD parent transaction (parent books the total amount of the batch) with validation errors to the Repair queue for user intervention or is cancelled automatically.  - Automatic cancellation is available only for TPH. - Additionally, it routes invalid batch children can to the Repair queue (similar to single DD that is based on specific configuration as part of a Netting Agreement, the *Repair**Batch**Child* field is set to Y). |

## Inward Processing of SEPA DD from Clearing

This section describes the processing of an incoming DD from a SEPA clearing, initiated or sent by the creditor’s bank.



| Activity | Description |
| --- | --- |
| Message format validation | Validates pacs.003 message format by checking mandatory and non-mandatory fields, proper field length and content based on pacs.003 XML definition language file (provided by the clearing). |
| Mandate validation | Validates the mandate for B2B DD and amends it (when the amendment information is provided with DD and *Mandate Amendment* is enabled in the Clearing Setting configuration).  - In Core DD, the mandate validation is optional (according to the scheme) and auto-mandate creation can be activated. - If the mandate does not exist in DD.DDI, canceled, expired, or exceeds the limit (based on periodicity and maximum amount), the system routes the DD to repair or rejects it (automatically).  To know more, refer to Repair or Automated Reject processing. |
| Debit account validation | Validates the following for the debit account:  - Is a valid Temenos Transact Account. - If the account is invalid, frozen or closed, or does not exist, it routes the DD to repair or rejects it (automatically).  To know more, refer to Repair or Automated Reject processing. |
| Dates calculation | Determines the collection or settlement date (as the *RCLD* is from the inward DD).  - If the *RCLD* is equal to or before the current business date, the collection or settlement date is set equal to the current business date. - If the determined collection or settlement date is a bank holiday, the system forwards the date to the first banking business day based on the cut-off shift day. - To configure one day in channel cut-off, go to **Admin Menu** > **Payment Hub** > **Routing And Settlement** > **Channel Cut-off Configuration**.   Calculates the debit and credit value dates and book date, which equals the determined collection or settlement date. |
| Duplicate check | Enables to configure the check on the following:  - *End-To-End Reference* (Customer Specified Reference) - *RCLD* - *Mandate Reference* - *Creditor ID* - *Transaction Amount* - *Incoming Message Type*   The values of these fields can be changed or configured based on the client requirement.  If the duplicate check fails, the system routes the DD to repair or rejects it (automatically)  To know more, refer to Repair or Automated Reject Processing. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. During a HIT from filtering, it routes the DD to repair. |
| Warehouse future dated | - Warehouses DD initiations or schedules for release on the calculated debit value date (which is equal to settlement or collection date). - Validations (except bulk agreement and message format) are repeated on release. |
| Balance check | Checks whether sufficient funds are available in the debtor’s account before posting an inward DD. If sufficient funds are not available, it performs the following:  - Cancels or rejects the DD transaction automatically - Routes to the Repair queue - System can retry checking till the *RCLD* or settlement date. |
| Posting | Debits the debtor’s account with the transaction amount. If posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or rejects it. To know more, refer to Repair. **Posting**   - Debit clearing suspense account is configured in Clearing Setting - Debit debtor is the client account   **Settlement Booking Entry**  If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Repair | Routes the inward DD with validation errors to the Repair queue for user intervention or rejects it (automatically). The user can repair the DD or reject it (manually) from the Repair queue. - Automatic reject processing is available only for TPH, which can be enabled using the clearing setting configuration. To know more, refer to Automated Reject Processing. - Automatic reject processing is performed when the following are not available:   - Debit account   - Mandate |
| Manual reject | Rejects the DD from the Repair queue (manually). System allows this only when the *Create Reject Message Indicator* field is configured in the Clearing Setting.   - To manually reject, go to **Admin Menu** > **Payment Hub** > **Local Clearing** > **Clearing Setting**. - In the *Error Information*, enter the reason code or description and then submit the DD from the Repair.   - The DD is authorised based on the authorisation principle. - The transaction can be rejected, when the current business date is before the settlement date or on the settlement date before the clearing reject cut-off time. |
| Automated reject processing | Rejects DD automatically when the *Automated**Return**Indicator* field is set as Y. Pre-condition –The current business date is before the settlement date or on the settlement date before the clearing reject cut-off time. |
| Original collection rejected | - Cancels DD and assigns status 998 (Rejected), when system rejects an inward DD (automatically or manually). - Updates the total bulk amount to be settled with the clearing at the determined settlement or collection date. |
| Generate and send pacs.002 message to clearing | Generates a pacs.002 reject message (or refusal message on behalf of the debtor) and sends it to clearing at the pre-defined clearing schedule. To know more, refer to Clearing Frequency configuration. |

## Inward Processing of SEPA DD Reject Messages from Debtor Bank



The status report message (pacs.003) has transaction information that is rejected or refused by a debtor for the corresponding original DD bulk (pacs.003) sent by a creditor bank.

| Activity | Description |
| --- | --- |
| Update status for the original outgoing DD bulk | Updates the status of the original DD bulk sent by the creditor bank to PART (partial), which indicates that an outgoing bulk has rejected transactions by the debtor bank. To view the status of the bulk, go to **User Menu** > **Payments** > **Payments Hub** > **Payment Inquiries** > **Received and Sent File Details** > **Sent File Details**. |
| Update amount to be settled for the original outgoing DD bulk | - Updates the pending settlement transaction of the original outgoing DD bulk, which is executed on a clearing settlement day (after reject cut-off time). - Books the settlement transaction with the total amount of the collections in the original pacs.003 bulk sent, minus the total amount of rejected transactions in the bulk. |
| Reject the original outgoing DD | Identifies and rejects the transactions based on the *Original Message ID* and *Original* *Transaction Reference* for each transaction in the pacs.002 message. If a rejected transaction is already booked (reject is received at the settlement date), the system generates a new reject transaction to refund the rejected amount. |
| Original collection marked as Returned | Marks the status of the original (returned) collection as ‘Rejected’ (998), after rejecting the incoming DD return. |

Reject messages with certain ISO reason codes can be routed to a manual ‘Reject’ or Clearing Status Report queue (if configured), which is not considered in this module.

## Inward Processing of SEPA DD Return or Refund from Clearing

This section describes the processing of an incoming DD return from a SEPA clearing, initiated or sent by the debtor’s bank, for the corresponding outgoing DD received from the creditor’s bank.



| Activity | Description |
| --- | --- |
| Message format validation | Validates pacs.004 message format by checking mandatory and non-mandatory fields, proper field length and content based on pacs.004 XML definition language file provided by clearing. |
| Debit account validation | Validates the following in a debit account:  - Is a valid Temenos Transact account - If invalid, frozen or closed, it routes the DD  to repair |
| Dates calculation | Determines the credit value date as the inter-bank settlement date of the DD return (if pacs.003 bulk is available). If the inter-bank settlement date is a bank holiday, the credit value date is determined as the first banking business day (based on the cut-off shift day). To configure one day in channel cut-off, go to **Admin Menu** > **Payment Hub**>**Routing and Settlement** > **Channel Cut-off Configuration**. Based on the configuration, the debit value date is when the return payment is processed or equal to the *Original Interbank Settlement* *Date*. |
| Duplicate check | Enables to configure the checks based on the following:  - *End To End Reference* (customer specified reference) - *RCLD* - *Mandate Reference* - *Creditor ID* - *Transaction Amount* - *Incoming Message Type*  If the check fails, the system routes DD to repair or rejects it (automatically). To know more, refer to Repair or Automated Reject Processing. |
| Identify original payment | Identifies the original outgoing payment transaction based on the *Original Message ID* and *Original Transaction ID* in the incoming return or refund message. If the original transaction cannot be identified or not fully processed, it routes the return DD to the Repair queue. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. During a HIT from filtering, it routes the DD to repair. |
| Balance check | Checks whether sufficient funds are available on the debtor’s account before posting the debit return. If sufficient funds are not available, it performs the following:  - Routes the DD transaction to the Repair queue - System can retry checking till the settlement date. |
| Fees calculation | The received return has bank charges (interchange fees and compensation refund cost) for the R-Message. These charges have to be paid to the original debtor bank. In TPH, these charges are debited from the customer (original creditor). The payment fails posting (debit side is not equal to credit side), when these charges are not setup for the product as client charges. |
| Posting | Debits the debtor’s account with the transaction amount. If posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or rejects it. To know more, refer to Repair. **Posting**   - Debit clearing suspense account is configured in clearing setting - Debit debtor is the client account   **Settlement Booking Entry**  If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Original collection marked as ‘Returned’ | Marks the status of the original (returned) collection as Completed and Returned (996), when the incoming DD return is booked. |
| Repair | Routes the inward DD with validation errors to the Repair queue for manual intervention (repair). It does not allow return or reject of an inward DD return. |

## Manual Return of Inward SEPA Payments



[Manual Return from the Repair Queue](#)

| Activity | Description |
| --- | --- |
| User initiates manual return or refund | Returns the DD from the Repair queue (manually), when:  - Inward SEPA direct debit cannot be booked on the settlement - Clearing cut-off time has already passed   - Direct debit is available or routed to the repair queue - Due to a posting restriction, closed or frozen account  To know more, refer to [Inward Processing of SEPA DD from Clearing](#Inward_Processing_of_SEPA_DD_from_Clearing). |
| User enters reason code or description in the Error Information tab and submit | Submits the DD from the Repair queue as ‘Returned’ with the reason code and description. Additionally, indicates whether the return is originated on behalf of the bank or debtor in the Error Information tab. The submitted transaction needs to be approved by another user from the Authorisation queue. |
| Timeline validation (acceptance days for returns) | Checks for maximum number of inter-bank business days allowed for a debtor bank to send return transaction after the settlement date of the original collection.  - B2B DD – 3 days - CORE DD – 5 days   This is configured in the Clearing Setting: Acceptance Days for Returns and the respective schemes. To know more, refer to [Configuration](Configuration.htm) section.  - System checks the timeline, the user submits the return from the Repair queue and sends a warning (if it exceeds). - The timeline is validated again, when the user authorises the submitted return from the Repair queue. |
| Posting – inward SEPA DD | Debits the original amount of the incoming DD from a return suspense account (instead of the debtor’s account) and credits the clearing suspense account, when:  - User submits the DD from the Repair queue as ‘Returned’ - Another user approves the submitted transaction |
| Creates new DD return | A new SEPA DD return is created when the inward DD is booked. |
| Posting – DD return | A new SEPA DD return is created with the following posting:  - Credit return suspense account is configured in the Clearing Setting - Debit clearing’s suspense account is configured in the Clearing Setting   **Settlement Booking Entry**  If SEPA returns are settled at the clearing settlement date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. This happens when the return file is sent to the clearing as returns are pre-settled. |
| Original collection marked as Returned | If an outgoing DD return is booked, it marks the status of the original (incoming and returned) collection as Completed and Returned (996). |
| Generate pacs.004 message | Generates a pacs.004 return message (or Refund message when it is returned on behalf of the debtor) and sends it to clearing at the pre-defined clearing schedule. To know more, refer to Clearing Frequency configuration. |

[Manual Return, Refund from the Return or Refund Page](#)

| Activity | Description |
| --- | --- |
| User initiates manual return or refund | The Operator can manually refund the original direct debit, when:  - Inward SEPA DD is already booked on the settlement date - Debtor requests the debtor bank to refund its account with the original collection amount  Go to **User Menu** > **Payments** > **Payments Hub** > **Payment Investigations and Cancellations** > **Return/Reject Payments** > **Return/Reject Inward Direct Debits**. |
| System creates new DD return in OE page | If the user selects and confirms the original outgoing DD to be returned or refunded, then it creates a DD return or refund transaction (for which the reason code and description can be entered). |
| User enters reason code or description in the Error Information tab and submit | - Submits the DD from the Repair queue as Returned with the reason code and description. - Additionally, indicates whether the return is originated on behalf of the bank or debtor (return or refund) in the fields in the Error Information tab.   The submitted transaction needs to be approved by another user from the Authorisation queue. |
| Timeline validation (Acceptance days for returns) | Checks the maximum number of inter-bank business days a debtor bank is allowed to send a return transaction, after the settlement date of the original collection.  - B2B DD – 3 days - CORE DD – 5 days - Refunds (only CORE scheme):   - Authorised mandate - 8 weeks + 2 inter-bank business days   - Unauthorised mandate - 13 months   The number of days are configured in the Clearing Setting (To know more, refer to [Configuration](Configuration.htm) section).  Checks the timeline when the user submits the return from the Repair queue and sends a warning (if the timeline exceeds).  The timeline is validated again when the user authorises the submitted return from the Repair queue. |
| Posting – inward SEPA DD | If a user submits the DD from the Return entry page as Returned, and another user approves and submits that the return is valid (time line), the following posting is applied:  - Credit return suspense account is configured in the Clearing Setting - Debit clearing’s suspense account is configured in the Clearing Setting   **Settlement Booking Entry**  If SEPA returns are settled at the clearing settlement date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account.  Debits the original amount of the incoming DD from a return suspense account (instead of the debtor’s account) and credits the clearing suspense account. |
| Posting –  DD return | Creates a new SEPA DD return with following posting:  - Credit original debtor’s account - Debit clearing’s suspense account is configured in the Clearing Setting   **Settlement Booking Entry**  If SEPA returns are settled at the clearing settlement date, the system checks and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Original collection marked as Returned | If an outgoing DD return is booked, it marks the status of the original (incoming and returned) collection as Completed and Returned (996). |
| Generate pacs.004 message | Generates a pacs.004 Return or Refund message (if returned on behalf of the debtor) and sends it to the clearing at the pre-defined clearing schedule. To know more, refer to Clearing Frequency Configuration. |

A pacs.004 return message is sent to the respective SEPA clearing, when returns are initiated from the Manual Repair page, or returned or refunded from the Return or Refund page. Similar to outgoing DD, the system performs the reachability check and SEPA channel validations (if configured).

## Supporting Continuous Gross Settlement Model

EBA STEP2 clearing was moved away from the net settlement model to the gross settlement model from November 2020. The new model is called the CGS, in which the multilateral batches received from the STEP2 participants are split bilaterally and settled instantly. The split files are then forwarded onward to the receiving participant instantly or as per the scheduled timings.

With the CGS model in STEP2, the processing of payment files and settlement of the resulting bilateral payment instructions takes place in real-time on transactions, one after the other. The bilateral payment instructions are also settled immediately if sufficient funds are maintained at the time of transaction or by the end of business day. Participants hold a funded position in STEP2 (the account holders have a positive account balance or minimum of zero), which is adjusted depending upon the settlement of each individual payment instruction and is completely backed by the funds in the central bank held on a technical account in TARGET2.

Participants can fund to and withdraw funds from their position throughout the day from the technical account in TARGET2 (if the TARGET2 account permits). Each participant can set upper and lower thresholds that are monitored by the system to initiate alerts when the set thresholds are reached.

Each of the STEP2 services interact independently with the CGS module. This interaction is activated only after the configuration of a Direct Participant within the CGS module, and the exchange of transactions, where both parties involved have activated the option in the service.

[Reconciliation Reports](#)

CGS module provides file-based interface that is used for system reporting, which provides reconciliation data related to the CGS Settlement BIC Liquidity Position to the STEP2 Preferred Agent BIC.

CGS provides the following reports to the defined participants:

| Sender | Business Level Message According to the Scheme | File Type | XML Message Used | XML Message Description |
| --- | --- | --- | --- | --- |
| CGS to STEP2 preferred Agent DP | Notification of the Participant Liquidity Position changing due to LCR and liquidity adjustments and operations processed | Liquidity Management Report (LMR) | camt.053 | Bank to Customer Statement |
| CGS to STEP2 preferred Agent DP | Notification of exceeding the configured thresholds | Liquidity Notification Report (LNR) | camt.052 | Bank to Customer Account Report |
| Notification of a liquidity adjustment | Liquidity Notification Report (LNR) | camt.054 | Bank to Customer Debit Credit Notification |

[Liquidity Management Report](#)

LMR is an optional XML file in the form of camt.053 generated and sent to all the configured CGS Settlement BICs (STEP2 Preferred Agent or Direct Participants). LMR is sent by the STEP2-CGS at the end of each Liquidity Adjustment Checkpoint (LAC) in order to notify about their liquidity position at the beginning and end of the relevant LAC.LMR files also include all the operations that have affected the liquidity position of the CGS Settlement BIC during the LAC.

LMR files will not be received and processed in TPH.

[Liquidity Notification Report](#)

- The CGS module generates LNR (an optional XML file) and sends to all the configured CGS Settlement BICs (STEP2 Preferred Agent Direct Participants) to be notified.STEP2 CGS sends liquidity adjustment notifications if there are funding or defunding actions occurring in the CGS position accounts. CGS sends the notifications called as LNR in the form of camt.054 to the account holding direct participant (as identified through CGS Preferred Agent).
- CGS sends LNR when thresholds are exceeded. The Liquidity Notification File also includes a camt.052 bulk to notify the participant that its liquidity position has exceeded the upper or lower thresholds set in the liquidity agenda for the current LAC.

TPH supports only LNR report (camt.054). LNR file, camt.052 are marked with status REJECTED.

[Liquidity Transfer Advice](#)

Temenos Payments Hub has the ability to receive LNR from the STEP2 CGS system. Temenos Payments Hub considers LNR as LTA, qualifies the LNR as a payment based on business rules, derive accounts for the market accounts within the notification and book them as payment Booking allows the bank to maintain the position of CGS Nostro account in-line with the account within CGS.

LNR may represent a credit advice or a debit advice depending on whether the participant banks account is credited or debited in the CGS Position Account due to liquidity transfer operations between the accounts.

- LNRs that fail processing are moved to the repair queue.
- LQ license is required to receive and process the LTA from STEP2.

[Qualifying the LNR as Payment](#)

When TPH receives a camt.054, it checks whether the transaction can be determined as payment or not based on the configurable criteria. The user can configure the qualification criteria using the following menu:

**Admin Menu** > **Payments** > **Liquidity Management** > **LTA Qualification**

| Criteria | Description |
| --- | --- |
| Sending Institution Identification | ID of the sending institution. |
| Receiving Institution Identification | ID of the receiving institution (typically a BIC of the bank). |
| Participant Identification | - Identification of the participant whose liquidity position or balance has been adjusted - This is the BIC of the bank (STEP2 preferred agent), in which the receiving bank is a direct participant or liquidity serviced participant. |
| Account Identification | Account of the participant whose liquidity position or balance has been adjusted (bank identifier or an account)  This is the account (held in STEP2-CGS), where receiving banks are a direct participant or liquidity serviced participant |
| Advice Type | Indicates whether the LTA is for a debit operation or credit operation     - Debit Indicator (DBIT) indicates debit on our account (found in the Debtor Account field in LTA) - Credit Indicator (CRDT) indicates credit on our account (found in the Credit Account field) |
| Transfer Type | Type of the underlying transfer, such as Regular Payment, AS transfer, or Liquidity adjustment |
| Local Instrument Proprietary | Identifies the proprietary type of underlying transaction. The values can vary by STEP2. For example, LIIA and LIIE |
| Local Instrument Code | Clearing-specific codes as received. For example, LIQT and LIQE |
| STEP2 Status Code | Status of the adjustments as recorded within the STEP2 system. For example, BOOK |
| Debtor Agent | Identifier of the agent who is getting debited. This can be STEP2 identifier (BIC) or the bank settlement’s BIC with TARGET2 (or the liquidity provider’s settlement BIC) depending on the LTA being debited or credited. |
| Debtor Account | Account identifier of the debtor agent who is getting debited. This can be STEP2 account or the account with STEP2 (or any of the liquidity serviced participant’s account in case the bank provides such service) depending on the LTA being debited or credited. |
| Creditor Agent | Identifier of the agent who is getting credited. This can be STEP2 Identifier (BIC) or the bank settlement BIC with TARGET2 (or the liquidity provider’s settlement BIC depending on the LTA being credited or debited. |
| Creditor Account | Account identifier of the creditor agent who is getting credited. This can be STEP2 account or the account with STEP2 (or any of the liquidity serviced participant’s account in case the bank provide such service) depending on the LTA being credited or debited. |

[Deriving Accounts for LNR](#)

For the LNR considered as a LTA, if qualified as a payment, the account for which the LNR notification is received is debited or credited in the participant bank that receives during the processing of the LTA payment.

LNR payment comprises a debit account and a credit account that represents accounts where the liquidity adjustments were affected by the Account Holding Institution. Both these accounts are external accounts to the bank, hence TPH resolves these accounts to an in-house Nostro or technical account within the bank to perform necessary bookings. The posting is mainly for liquidity management purposes, such that receiving participant bank’s Nostro balances are up-to-date with the balance or positions in the actual account in STEP2, enabling the receiving participant bank to perform efficient liquidity management functions.

The user can configure the in-house Nostro or technical account in account mapping table from the following menu

**Admin Menu** > **Payments** > **Liquidity Management** > **LTA Account Mapping**

[Handling LNR from Repair Queue](#)

Incoming LNR’s that failed to qualify as a payment or failed while resolving the account or failed duplicate check are moved to a repair queue for repairing by the bank user. Banks can also make the LNR payments as non-STP and can process from the repair queue. The user can view the incoming LNR’s awaiting repair using the dedicated enquiry –LTA Repair in TPH (Read the [Working with](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Working_wtih.htm) section for more information) .

From the repair screen, the user can either cancel the LNR or modify and submit to continue processing with repaired details.

The following fields can be modified during the repair:

- Value Date
- Debit Account
- Credit Account

Once the user repairs the payment and commits, it is moved to the supervisor’s queue for authorisation (if configured). After authorisation, the repaired payments is processed by the user again starting from the LTA qualification step.

If the user cancels the LNR, the LNR is moved to cancelled (997) status on authorisation. The user must enter the reason for cancelling.

Read the [Liquidity Transfer Advice](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Working_wtih.htm) guide for more details on configuring, viewing, and repairing LNR.

## Indirect Participation in SEPA

Processing of Direct Debit (DD) instruction to Indirect Participants (IP) is done in the same way as a DD received for Direct Participants (DP). However, on successfully processing the DD, the request is sent to IP in a separate file.

Direct Debit Instruction pacs.003 is received from Clearing in debit notification file. The file is validated against XSD and if accepted and Debulking is performed. In case of validation failure, the file is rejected. If the user determines the processing company’s Bank Identifier Code (BIC), then follow the existing DD processing.

Inward Debit Requests are received earliest fourteen calendar days prior to settlement date (D-14) and latest in D-1 days prior to settlement date (D), where D is the date when the debtor’s bank is debited by the SEPA Clearing. Based on mapping into neutral format and then into Temenos Payment Hub (TPH) format, the individual DD transactions are processed in the system.

If the debtor BIC is IP BIC, then the clearing is determined as IP. On the day of receipt, initial validation of the payment (if enabled), duplicate check and so on are performed in order to ensure that the payment can be rejected as early as possible. In case the functional validation is not successful on the day of receipt, the payment is rejected and sent to the clearing or the payment is routed to repair depending upon the clearing configuration in the system.

In case of any functional validation failure on the settlement date,

- payment is forwarded to IP based on clearing configuration
- payment is rejected (if before cut of time for R – messages on the settlement date)
- payment is returned (if after cut of time for R – messages on the settlement date)

For redirected payments received from the clearing that need to be routed an IP, the IP channel for direct debits to which the IP BIC is associated must be retrieved from the channel selection table. Each payment received from the clearing has a product defined in the system. This product has a corresponding routing product. For this routing product, a record is defined in the `PP.RS.CHANNELSELECTION` table.

The amount is debited from the debtor only on the settlement date and not on the date of receipt (that is, amount reservation is performed on settlement date).

The posting of a valid direct debit is as follows:

- Debit IP channel suspense account
- Credit EBA Nostro Account

Settlement transaction are created based on the incoming DD and redirected to IP (Post Settlement Clearing Mechanism. This means that a pending settlement record is created per bulk on the day of receipt but released and executed on the future (requested) settlement date after the clearing cut-off time for rejects. The pending settlement record amount (value) is the total amount for all messages that the pacs.003 bulk contains. The amount of any rejected debit requests and refusals by debtor is subtracted from the total settlement amount of the corresponding pending record before the execution date (settlement date).

After the clearing cut-off time for rejects in the settlement date, the pending settlement record is released and a payment order is created in the system. At the pre-scheduled time defined for the IP channel for direct debits (same time for all IP), the direct debits waiting to be sent through the IP channel are bulked and sent. One DD pacs.003 is created for each IP. The CORE and B2B service level payments are sent in separate files to an IP. The number of bulks in a file and number of transactions in a bulk, and the max number of files in a cycle can be defined per IP (configurable).

## Illustrating Model Parameters

To know more on parameter setup for Single Euro Payments Area (SEPA) direct debit, refer the [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

This module provides the facility to send and receive SEPA Direct Debit requests from STEP2 and RPSSCL clearing.

In this topic

- [Introduction to SEPA Direct Debit](#IntroductiontoSEPADirectDebit)

- [Business Events, Transaction Types, and Message Types](#BusinessEventsTransactionTypesandMessageTypes)
- [Post and Pre-Settled](#PostandPreSettled)
- [SEPA DD Schemes](#SEPADDSchemes)
- [DD Batches versus Single DD](#DDBatchesversusSingleDD)
- [Recurrent and One-Off DD](#RecurrentandOneOffDD)
- [SDD Mandate Validation](#SDDMandateValidation)
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
- [Supporting Continuous Gross Settlement Model](#SupportingContinuousGrossSettlementModel)
- [Indirect Participation in SEPA](#IndirectParticipationinSEPA)
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
Tuesday, April 14, 2026 4:19:43 PM IST