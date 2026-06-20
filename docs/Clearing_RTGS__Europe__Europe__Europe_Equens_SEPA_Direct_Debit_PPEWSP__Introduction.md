# Introduction to Equens SEPA Direct Debit

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Equens SEPA Direct Debit](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Introduction.htm) > Introduction

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
  - [MAV Payments MAV Payments](../../Europe/Europe_MAV_Payment_PPCLIT/Introduction.htm)
  - [Equens SEPA Direct Debit Equens SEPA Direct Debit](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Introduction.htm)
    - [Introduction](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Introduction.htm)
    - [Configuration](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Configuration.htm)
    - [Working with](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Working_with.htm)
    - [Tasks](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Tasks.htm)
    - [Outputs](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Outputs.htm)
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

# Introduction to Equens SEPA Direct Debit

Updated On 20 January 2026 |
 75 Min(s) read

Feedback
Summarize

Equens is the central clearing institute for retail payments. The bank can use this setup to promote and maintain efficient payment processing and reliable payment system. Temenos offers pan-European market coverage (due to clients and partnerships in many European countries) for payment processing from offices in four countries, such as Netherlands, Germany, Italy and Finland.

The Clearing and Settlement Mechanism (CSM) is classified into three categories:

- National
- Regional
- Pan European

The Equens CSM is a regional CSM in Netherland for clearing of SEPA payments. Payments destined for other participants of the Equens CSM are settled within same community. Equens offers clearing and settlement of Single Euro Payments Area (SEPA) payments as SEPA Credit Transfer (SCT) and SEPA Direct Debit (SDD), and settles the payments in Trans Automated Real Time Gross Enable Transfer System (TARGET2). Equens SDD is based on SEPA scheme that has the changes published in the Equens clearing specifications.

Single Euro Payments Area (SEPA) initiative was created to support Electronic Euro payments. It make it easy and convenient for citizen and business to pay across Europe with one payment account and card from their home countries. The European Payment Council (EPC) has created the implementation standards and rule books for SEPA. It has four Euro payment schemes:

- Credit transfer
- Direct debits (DD) core scheme
- DD business-to-business scheme
- Instant credit transfer

The area in which these payment schemes (for all euro credit transfers and DD) are available is broader than the European Union. It covers 36 countries and territories, such as 28 Member States plus Iceland, Norway, Liechtenstein, Switzerland, Monaco, San Marino, Andorra and Vatican City State or Holy See. The following sections describes the usage and configuration of SEPA CORE and Business-to-Business (B2B) DD scheme transactions:

To know more about DD and its uses, refer to [Direct Debits](../../Payments_Hub_(PP)/Direct_Debits/Introduction.htm#top).

Temenos Payments Hub (TPH) SEPA DD supports the following:

| Business Event | Transaction Type | Description | ISO Message | Version |
| --- | --- | --- | --- | --- |
| DD transfer initiation | DD | - Receives and executes Customer-to-Bank DD collection requests. - Validates the request received from the creditor and routes it through appropriate clearing (when the debtor belongs to another bank), based on the Requested Collection Date (RCLD), cut-off time, and days required for the clearing to finally settle the amount. - Warehouses the payments with a future value date and processes on the due date. - Forwards the finalised payment to clearing in pacs.003 message format or other supported native clearing format. - Raises settlement entries at the RCLD or settlement date. | pain.008 or initiated through Order Entry (OE) DD book or outgoing page | 02 |
| DD | DD | - Receives and processes Bank-to-Bank DD payment orders to debit the debtor in the books of the processing bank. - Executes DD successfully, when it:   - Supports debit instruction with appropriate mandates   - Has sufficient funds in the debtor account - Otherwise, the debit item is rejected or returned. | pacs.003 | 02 |
| DD reject | RJ | - A negative confirmation of direct debit item received by the debtor bank. - Payments Hub (PH) can perform the following:   - Send an outbound DD rejection message (pacs.002), when DD instruction from clearing cannot be processed successfully (for example, the debtor mandate is not available and funds are insufficient in the debtor account).   - Allow the transformation of rejection messages in non-ISO format to support native clearing formats.   - Receive inbound DD reject message (pacs.002) and mark the previously sent collection item as Rejected (which are excluded for Settlement). | pacs.002 | 03 |
| Return debit transfer or DD | RF | - Enables the return of DD after the settlement date, when it is within the allowed time period of the clearing. It is initiated by the debtor bank. - Temenos Payment Hub (TPH) performs the following:   - Supports automated and manual return of incoming DD that are unsuccessful.   - Generates pacs.004 or other native clearing message format for supported outgoing returns clearing.   - Supports DD returns received by the creditor bank for previously originated debits.   - Receives the returns as pacs.004 messages and process them as STP.   - Supports native clearing formats for DD returns as a feature of the relevant clearing. | pacs.004 | 02 |
| Debit refunds | RD | - DD can be returned manually at the request of the debtor, within the allowed time period when supported by the clearing. - TPH perform the following:   - Generates pacs.004 message for outgoing DD refunds.   - Supports native clearing formats for DD refund in the respective Clearings.   - Supports receipt of DD refunds from debtor bank by using clearing and processes them by debiting the creditor who initiated the DD. | pacs.004 | 02 |
| Customer payment (DD) reversal | RV | - Creditor Bank can receive a payment (DD) reversal request (pain.007 message) from the creditor. - TPH can perform the following:   - Support the receipt of customer payment reversal message (pain.007) to reverse a previously initiated DD.   - Reversals accepted are processed STP by debiting the creditor (initiating the reversal) and crediting the beneficiary.   - Generates an outgoing pacs.007 message for DD reversals to clearing.   - Supports the native clearing formats in the relevant clearing feature. | pain.007 or initiate a reversal of a processed DD through OE | 02 |
| DD reversal | RV | - Debtor bank can receive an incoming DD reversal from the creditor bank through the clearing. - TPH can receive DD reversals (pacs.007) and credit the debtor account. | pacs.007 | 02 |
| DD cancellation | CS | Originator bank sends SEPA collection request to Equens clearing, which is recalled by sending a camt.056 message. The originator (creditor) of the DD or originator (creditor) bank of the DD initiates the DD cancellation request. TPH supports initiating a cancellation request for the incoming collection request. | camt.056 | 02 |

## Post and Pre-Settled

This section helps the user to understand the post and pre-settlement.

[Pre-Settlement](#)

SEPA DD is initiated and sent to clearing pre-settlement (one interbank business day and maximum 14 days before the request collection or settlement date). It is booked or settled on the request collection or settlement date. Settlement booking entries to the clearing Nostro account occur on the settlement date (RCLD) for the total amount of DD (each DD bulk sent to the clearing) considering all the rejections till the settlement date. DD can be cancelled by the creditor’s bank or rejected by the debtor’s bank (or refused by the debtor through debtor bank) pre-settlement (before the clearing reject cut-off).

[Post-Settlement](#)

After clearing settlement, DD (processed or completed and settled by the clearing) can be reversed by initiating DD reversal by the creditor bank, returned by the debtor bank or refunded by the debtor (through debtor’s bank). The debtor can initiate the timeline (period) within a refund depending on the authorisation or unauthorisation of DD mandate.

The below diagram shows the classification of pre-settlement and post-settlement messages.



## SEPA DD Schemes

The following are the two types of schemes in SEPA DD:

| Scheme | User | Description |
| --- | --- | --- |
| SDD B2B | Consumer (CORE) | Debtor bank needs to check the mandates according to the SDD rule book by EPC. Hence, refund option is not available for the debtor. |
| SDD CORE | Business (B2B) | Debtor bank needs to check the mandates as an additional or optional service. Hence, refund option is available for the debtor. |

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

## Pre-Settlement SDD Events or Messages

The below table portrays SEPA DD events or messages before clearing settlement, as a set of steps and events in the order of occurrence. It includes all the rejects, refusals or cancellation requests of a DD transaction (Pre-settlement R-messages).

| Business Event or Timeline | Creditor | <--> | Creditor Bank | <--> | Clearing Settlement at Settlement Date (D) | <--> | Debtor Bank | Debtor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD initiated: <*RCLD-14C* | Initiate DD | --> pain.008 | Warehouses and releases at RCLD-14C | --> pacs.003 | Scheduled at *D*=RCLD | --> pacs.003 | Receives at D-14 | Option for refusal |
| DD initiated: > RCLD-14C and <= RCLD-1TD | Initiate DD | --> pain.008 | Validates and sends the message to clearing on the same day. DD scheduled at due date or book date = RCLD | --> pacs.003 | *D*=RCLD | --> pacs.003 | Receives on the same day, the creditor initiates the DD | Option for refusal |
| DD initiated: *RCLD* | Initiate DD | --> pain.008 | Validates and sends the message to clearing on the same day. DD scheduled at due date = RCLD+1C | --> pacs.003 (with *RCLD* = *RCLD+1C*) | *D* = RCLD+1 | --> pacs.003 | Receives on the same day, the creditor initiates the DD | Option for refusal |
| DD refused by debtor: <= *D* before reject cut-off |  | <-- pain.002 (optional based on configuration) | Rejects DD transaction. Do not settle register transaction at D | <--pacs.002 | Do not settle register transaction at *D* | <--pacs.002 | Refusal message initiated on behalf of the debtor | Request for refusal to the bank |
| DD reject by debtor bank: <=*D* before reject-cutoff |  | <-- pain.002 (optional based on configuration) | Rejects DD transaction. Do not settle register transaction at *D* | <--pacs.002 | Do not settle register transaction at *D* | <--pacs.002 | Rejects message initiated on behalf of the debtor bank |  |
| DD cancellation request by creditor bank: <= *D* before reject-cutoff |  |  | Initiates cancellation request on behalf of creditor or bank | --> camt.056 | Do not settle register transaction at *D* | --> camt.056 | Rejects DD transaction. Do not settle register transaction at *D* |  |
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

The outgoing SEPA Equens DD payments is clubbed based on the requested collection or interbank settlement date. This generates different files for different requested collection dates. It does not allow to club different payment types to a single file. For example, pacs.003, pacs.004, pacs.002, camt.056 and pacs.007 cannot be clubbed to the same file. However, it is bulked as two separate bulks in the same file.

CORE and B2B payment scheme is not clubbed into the same file.

## Outward Processing of DD Initiation (pacs.003)

This section describes the outward processing of a DD order initiated in TPH or ordering bank.



| Activity | Description |
| --- | --- |
| Manual capture of SEPA DD initiation from branch or back office by using OE page | - Captures a SEPA DD from TPH OE page. - Validates (mandatory and non-mandatory) fields and inputs data on submission. |
| Outgoing DD payment instructions through ordering bank | Sends DD payment instructions to TPH bank through ordering party’s bank (same as TPH bank or another bank). The instruction is in the pain.008.001.02 – ISO20022 format. |
| File duplicate check | Checks whether a file is received from a channel other than TPH OE. If a duplicate file is found, it rejects and sends a negative pain.002 message to the initiating bank or system (if configured). This check is based on the following combination of fields in the pain.008 file:  - Group header message identification - Message format of the file - Group header initiating party organisation IDBIC - Source from which the pain.008 file is originated |
| Format validation | Validates the pain.008 message format by checking mandatory and non-mandatory fields, proper field length, and content based on pain.008.001.02 XML definition language. |
| Bulk agreement validation | - Validates pain.008 bulks against a netting agreement setup for the submitter of the bulk. - To perform this, go to **Admin Menu**>**Payment Hub**>**Debit Authority**>**Netting Agreements**.   - Netting agreement validation can be skipped when the *Message* *Type* (pain.008) is configured in the No DA List (in the Debit Authority menu). - Bulk agreement validation is not applied for DD initiated from TPH OE page.  To know more, refer to Bulk or Netting Agreement. |
| Credit account validation | Validates the following for the ordering account:  - Is a valid Temenos Transact account - Has a posting restriction |
| Execution warehouse | Warehouses DD initiations that are received 14 calendar days (or more) prior to the RCLD (which is configured in *Max Allowed Days* in Source settings) or scheduled for release on RCLD minus 14 calendar days. The following is performed in a DD batch that is received 14 calendar days (or more) before RCLD:  - Warehouses the parent (total amount) transaction - Creates child transactions from the batch when the parent transaction is released and validates it successfully |
| Determine SEPA outgoing clearing | - Determines the outgoing clearing channel from the RS Channel Selection List. - To access this, go to **Admin Menu**>**Payment Hub**>**Routing and Settlement**. - The clearing suspense account is determined for the respective outgoing SEPA clearing channel (for example, STEP2). |
| Reachability check | Validates whether the debtor bank (BIC) is reachable through the selected SEPA clearing. To know more, refer to [Reachability](../../Payment_Initiation_(PI)/Reachability/Introduction.htm). |
| SEPA channel validations | Performs this validation on the DD to ensure that it meets the compliance requirements of the SEPA clearing. The following fields are validated or need to be mandatory:  - *Local Instrument Code* - *Sequence Type* - *Transaction Amount* - *Transaction Currency Code* (needs to be equal to EUR) - *Details of Charges* (needs to be equal to SHA or SLEV) - *RCLD* - *Mandate Identification* - *Mandate Date Of Signature* - *Creditor ID* - *Creditor Name* - *Creditor Account* (a valid IBAN) - *Creditor ID* - *Debtor Name* - *Debtor Account* (a valid IBAN) - *Debtor Agent BIC* (available or system-driven) |
| Dates calculation | Calculates the DD (debit and credit) value dates and booking date. Basics rules for date calculation for outgoing transactions are as follows:  - If the *RCLD* of the DD initiation is equal to or before the current business date, the collection or settlement date is set one banking business date ahead from the current business date (based on the configured settlement shift for the respective SEPA clearing, which is 1 day for both CORE and B2B scheme DD). - If the clearing cut-off time has already passed when applying the settlement shift, the system applies another cut-off shift day (1 day).   To configure the settlement and cut-off shifts, go to **Admin Menu**>**Payment Hub**>**Routing and Settlement**>**Channel Cut-off Configuration**.  Calculates the debit and credit value dates and book date, which is equal to determined collection or settlement date. |
| Duplicate check | Enables to configures the check based on the following criteria: DD batch booking (parent transaction that books the total amount)   - *Account of the credit party* - *Currency of the credit account* - *Transaction amount* - *Currency* - *RCLD* - *Bulk reference*  Each DD transaction in a batch  - *Account of the debit party* - *Currency of the debit account* - *Transaction amount* - *Transaction currency* - *RCLD* - *Instruction identification*  Single outgoing DD transaction (batch booking is false)  - *Account of the credit party* - *Currency of the credit account* - *Transaction amount* - *Transaction currency* - *RCLD* - *Instruction identification*   The system can configure and change (if required) the duplicate checks. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank specific requirement and is performed in the site.  TPH solution is pre-integrated with Temenos Financial Crime Mitigation (FCM) solution. |
| Generate and send pacs.003 to clearing | Bulks DD initiations and sends a pacs.003 message to the respective SEPA clearing, when:  - DD transactions are received at least 14 days prior the given *RCLD* - All business validations are qualified |
| Warehouse future dated | Warehouses DD initiations or schedules for release on the calculated debit value date (which is equal to settlement or collection date). |
| Fees calculation | Charges creditor for any fees. Fees for child DD transactions are booked or posted (similar to single DD transactions and not along with batch parent transaction). |
| Posting | Credits the creditor’s account with the transaction amount.  If the posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or is cancelled. **Posting**   - If a DD initiation is a child of a batch (booking indicator is true or configured as a part of the netting agreement), then:   - Debit clearing suspense account is configured in Clearing setting   - Credit batch suspense account is configured for each company - If a DD initiation is a single transaction (booking indicator is false or configured as a part of the netting agreement), then:   - Debit clearing suspense account is configured in Clearing setting   - Credit creditor is the ordering client - Total requested bulk amount of a batch booking transaction is known as the parent transaction of the batch children, in which:   - Batch suspense account is configured for each company   - Credit creditor is the ordering client   **Settlement Booking Entry**   - If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Error queue | Rejects batch child transactions with validation errors by performing the following posting on the settlement or collection date:  - Debit creditor is the ordering client - Credit batch suspense account is configured for each company  Routes single or parent transaction (parent books the total amount of the batch) with validation errors to the Repair queue for user intervention or is cancelled automatically. - Automatic cancellation is available only for TPH. - Additionally, it routes invalid batch children to the Repair queue (similar to single DD that is based on specific configuration as part of a Netting Agreement, the *Repair**Batch**Child* field is set as Y). |

## Book Processing of DD Initiation

This section describes the processing of a DD book order initiated in TPH or ordering bank.



| Activity | Description |
| --- | --- |
| Manual capture of SEPA DD initiation from branch or back office by using OE page | - Captures a SEPA DD from TPH OE page. - Validates mandatory and non-mandatory fields and inputs the data on submission. |
| Outgoing DD payment instructions through ordering bank | Sends DD payment instructions to TPH bank through ordering party’s bank (same as TPH or another bank). The instruction is in pain.008.001.02 – ISO20022 format. |
| File duplicate check | Checks whether a file is received from a channel other than `PAYMENT ORDER` (`PO`) application or TPH OE. Rejects the file (if it is a duplicate) and sends a negative pain.002 message to the initiating bank or system (if configured). This check is based on the following combination of fields in the pain.008 file:  - Group header message identification - Message format of the file - Group header initiating party organisation Id BIC - Source from which the pain.008 file is originated |
| Format validation | Validates the pain.008 message format by checking mandatory and non-mandatory fields, proper field length and content based on pain.008.001.02 XML definition language. |
| Bulk agreement validation | - Validates pain.008 bulks against a netting agreement setup for the submitter of the bulk. - To perform this, go to **Admin Menu**>**Payment Hub**>**Debit Authority**>**Netting Agreements**.   - Netting agreement validation can be skipped when the *Message Type* (pain.008) is configured in the No DA List (in the **Debit Authority** menu). - Bulk agreement validation is not applied for DD initiated from TPH OE page.  To know more, refer to Bulk or Netting Agreement. |
| Credit account validation | Validates the following for the ordering account:  - Is a valid Temenos Transact account - Has a posting restriction |
| Execution warehouse | Warehouses DD initiations that are received 14 calendar days (or more) prior to the *RCLD* (which is configured in *Max Allowed Days* in Source settings) or scheduled for release on RCLD minus 14 calendar days. The following is performed in a DD batch that is received 14 calendar days (or more) before RCLD:  - Warehouses the parent (total amount) transaction - Creates child transactions from the batch when the parent transaction is released and validates it successfully |
| Debit account validation | Validates the following for the debtor account:  - Is as valid Temenos Transact account - Has a posting restriction |
| Dates calculation | Calculates the DD (debit and credit) value dates and booking date.  - If the *RCLD* of the DD initiation is equal to or before the current business date, the collection or settlement date is set one banking business date ahead from the current business date (based on the configured settlement shift for the respective LEDGER, which is 1 day for both CORE and B2B scheme DD). - If the clearing cut-off time has passed when applying the settlement shift, the system applies another cut-off shift day (1 day).   To configure the settlement shift and cut-off shift, go to **Admin Menu**>**Payment Hub**>**Routing and Settlement**>**Channel Cutoff Configuration**.  Calculates the debit and credit value dates and book date, which equals the determined collection or settlement date. |
| Duplicate check | Enables to configure the check based on the following criteria: DD batch booking (parent transaction that books the total amount)   - *Account of the credit party* - *Currency of the credit account* - *Transaction amount* - *Currency* - *RCLD* - *Bulk reference*   Each DD transaction in a batch   - *Account of the debit party* - *Currency of the debit account* - *Transaction amount* - *Transaction currency* - *RCLD* - *Transaction identification*   Single book DD transaction (batch booking is false in the DD)   - *Account of the credit party* - *Currency of the credit account* - *Account of the debit party* - *Currency of the debit account* - *Transaction amount* - *Transaction currency* - *RCLD* - *Transaction identification*   The system can configure and change the duplicate checks. |
| Warehouse future dated | Warehouses DD initiations or schedules release on the calculated debit value date (which is equal to settlement or collection date). |
| Fees calculation | Charges creditor and debtor for any fees (if configured). Fees for child DD transactions are booked or posted (similar to single DD transactions and are not posted along with the batch parent transaction). |
| Balance check | Checks whether sufficient funds are available in the debtor’s account before posting a DD transaction (child of a batch or single DD).  - If sufficient funds are not available, it performs the following:   - Cancels or rejects the DD transaction (automatically)   - Routes to the Repair queue   - System can retry checking till the *RCLD* or settlement date. The system can be configured to retry debiting the debtor’s account even a few days after the settlement date (based on *Settlement* *Retry Days* configured as part of a netting agreement). - If sufficient funds are not available in the debtor’s account on the settlement date and any configurable settlement retry days, the system rejects the DD. |
| Posting | Credits the creditor’s account with the transaction amount. If posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or is cancelled. **Posting**   - If a DD initiation is a child of a batch (batch booking indicator is true or configured as a part of the netting agreement), then:   - Debit clearing suspense account is configured in Clearing Setting   - Credit batch suspense account is configured for each company) - If a DD initiation is a single transaction (batch booking indicator is false or configured as a part of the Netting Agreement), then:   - Debit clearing suspense account is configured in Clearing setting)   - Credit creditor is the ordering client - Total requested bulk amount of a batch booking transaction is known as the parent transaction of the batch children, in which:   - Batch suspense account is configured for each company)   - Credit creditor is the ordering client   **Settlement Booking Entry**  If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Error queue | Rejects batch book child transactions with validation errors by performing the following posting on the settlement or collection date:  - Debit creditor is the ordering client) - Credit batch suspense account is configured for each company)   Routes single transactions or DD parent transaction (parent books the total amount of the batch) with validation errors to the Repair queue for user intervention or is cancelled automatically.  - Automatic cancellation is available only for TPH. - Additionally, it routes invalid batch children can to the Repair queue (similar to single DD that is based on specific configuration as part of a Netting Agreement, the *Repair**Batch**Child* field is set to Y). |

## Outward Processing of Rejected DD (pacs.002)

TPH as a debtor bank generates the outgoing Reject for the incoming DD collection request (pacs.003). After processing, the outward reject transaction or file sent to Equens clearing and the amount of the transaction is not booked from the customer account.



| Activity | Description |
| --- | --- |
| Outgoing reject or refusal (pacs.002) from TPH enquiry to Equens CSM | Sends reject or refusal message for the underlying incoming collection request. Outgoing DD reject is sent prior to the settlement (pre settled R-message). The creditor bank receives a reject, when the debtor bank is unable to debit the debtor for the following reasons:  - Insufficient funds, account is closed, account restrictions, and invalid mandate - Refusal (by the debtor) before the settlement date |
| Reject the original incoming DD | Generates the outgoing reject transaction (pacs.002) with the underlying incoming collection request message ID and transaction reference available in the pacs.003.  - If the incoming collection request is already booked (reject is sent on the settlement date), the system generates a new reject transaction to refund the rejected amount. - If a reject is sent for DD collection in a batch (one debit with multiple credits), the system creates the following:   - Individual reject transaction   - Consolidated reject transaction or all rejects till the settlement date (based on the agreement with the clearing) |
| Adjustment to the incoming collection request amount | Sends an outgoing reject message to Equens clearing before the settlement of incoming collection request. |
| Original Incoming collection status marked as ‘Rejected’ | Updates the status of the incoming collection request transaction or bulk to Rejected (998). |

## Outgoing Processing of Cancellation Request (camt.056)

Creditor bank can trigger outward cancellation request (camt.056) to debtor bank before the reject cut-off time on the settlement date. However, the debtor bank cannot reject an incoming cancellation request.



| Activity | Description |
| --- | --- |
| Create cancellation request (EBQA page) | Bank Operator initiates a Recall request (for an already sent outward collection - pacs.003) as bank or customer initiated recall request. In the Cancellation Initiation Inquiry, TPH displays the list of outgoing collections for which the user can raise a cancellation request (sent to the clearing). |
| Validate cancel request | Enters the reason for initiating the cancellation request. TPH validates the reason codes and other fields as mandated for each Equens SEPA CSM (customised for each CSM). System checks whether the validation is raised before the reject cut-off time on the settlement date. |
| Create cancellation request | Creates the cancellation request in the system (if validation is successful) |
| Authorise cancellation request (EBQA page) | Supervisor authorises the recall when 4-eye principle is configured. System checks if it is within the sending reject cut-off time raised in the settlement date. |
| Request processing | If the creditor is not credited for the collection, system cancels the collection and adjusts the settlement amount in the pending settlement record for the pre-settlement R-message amount. If the creditor is already credited, system creates a reversal transaction where the original creditor is debited. When a cancellation request is received for direct debit collection of a batch (one credit - multiple debits), it creates:   - An individual reject transaction - A consolidated reject transaction for all R-messages processed till the settlement date   This can be single or consolidating booking based on the agreement with the customer. |
| Bulking and generating camt.056 | Generates camt.056 during the clearing settlement (configuration for each CSM and message type). Each CSM can have its own XSD and mapping requirements. Bulks camt.056 message waiting to be sent  to CSM (there is no other criteria for bulking) Business-to Business (B2B) and CORE is sent as separate files. |
| Send status to the customer | Reflects cancelled collection in the status report sent to the customer(pain.002), which is based on the agreement with the customer |
| Error | If there is a validation failure during cancellation request creation, it displays the error on the bank operator’s page |

## Outgoing Processing of Reversals (pacs.007)

The creditor can generate reversal on request after the due date requested in the original collection. In TPH, the creditor’s bank can initiate reversals for the following:

- pain.007 received from client channels
- DD collection from DD Reversal page in TPH



| Activity | Description |
| --- | --- |
| Reversal  initiation through pain.007 message | Initiates an Equens SEPA reversal by sending a pain.007 to the creditor bank |
| Receive and map | Receives, validates and maps the pain.007 message in TPH. This message can have one or more customer batches.  If the validation of message format fails, it moves to the Error queue.  When bulk agreement is validated, TPH checks whether the submitter or issuer (creditor) has an agreement to send the pain.007 file.  - If the bulk agreement validation fails, it routes the file to the Error queue. - If the original DD collection file or bulk is not located in the system, the file or bulk is sent to the Error queue. |
| Debulking and look up of original collection | If pain.007 is a batch payment, it is debulked to single reversals. System decides whether to process transactions in bulk as individual transactions (single debit - single credit or as a batch (single debit - multiple credits), based on the batch indicator in the file (pain.007) or bulk agreement. If the individual reversal request is not matched to underlying debit collection or the original collection is not fully processed, the system performs the following:  - Single Reversal – Cancels the individual reversal request (automatically) or routes it to the Repair queue (based on configuration) - Batch Reversal – Reverses the individual reversal request in the batch (automatically), where the customer is credited again  System checks whether the reversal is received within the allowed acceptance days. If the validation fails, it cancels or moves the request to the Repair queue |
| Manual capture of Equens SEPA DD reversal from branch | Initiates reversal for an already processed DD collection from the DD Reversal page. System validates the following:  - Mandatory and non-mandatory fields on submission and displays an error (if any) - Triggers reversal before the allowed time lines (five interbank days after the settlement date of underlying collection) |
| Creation of a reversal transaction | Creates reversal transaction (RV transaction type) for reversed collection |
| Debit account validation | Validates whether the debit account is a valid Temenos Transact account (or from a bank specific account with systems that have local site-specific functionalities) and does not have any posting restrictions. |
| Routing | Routes the payment to an Equens SEPA clearing channel (which moves it to SEPA DD reversals). Clearing channel determines the message type (pacs.007). |
| Reachability check | Validates whether the receiving bank is reachable directly or indirectly (if configured) through the selected Equens SEPA CSM for the DD reversal |
| Equens SEPA channel validations | Performs all Equens SEPA specific validations on the transaction to ensure reversal meets the compliance requirements of SEPA DD reversal scheme (such as IBAN is mandatory and valid, address details available, currency is EUR, charge option is SHA) |
| Dates calculation | Calculates the remaining dates (such as book date, debit value date, floats - configurable) and send date (configurable). - Booking date needs to be equal to the processing date - Send date needs to be equal to the settlement date (credit value date) - Debit value date needs to be configured based on processing date (considering the configured floats) |
| Duplicate check | Enables to configure the check on the set of payment attributes, such as payment amount, currency, and transaction reference |
| Sanction screening | Performs sanction screening of payments when interfaced to a screening engine. This is a bank specific requirement and is performed in the site. TPH solution is pre-integrated with Temenos FCM solution. |
| Fee calculation | Calculates the applicable charges (if configured) |
| Balance reservation | Reserves funds on the debit account. Balance reservation is done on payment amount with charges. TPH checks whether the debit account has no posting restrictions.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Posting | Debits the original creditor’s account with payment amount and charges to be borne by the customer. If posting fails due to insufficient funds, it parks the payment in Repair queue for user action (Reject or Cancel) or automatic retry based on configuration.  - If AMS is Temenos Transact, then TPH performs debit posting in embedded mode. - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  Outward reversals entries are made before sending pacs.007 to Equens SEPA CSM. Credit Transaction Entries (Single accounting)   - Debit debtor account - Credit CSM suspense account  Credit Transaction Entries (Single debit – multiple credit accounting) Total batch amount   - Debit debtor account - Credit batch suspense account  Individual transactions in the batch  - Batch suspense account - Credit CSM suspense account |
| Park for distribution | After raising the accounting entries, it parks the reversal and sends them to the CSM at pre-defined frequency (which is based on the Settlement page) |
| Bulking | Bulks the transactions into batches according to the bulking configuration defined for the CSM. This includes file and bulk naming convention, number of bulks in a file and transactions in a bulk.  Reversals for the CSM is bulked based on settlement date (credit value date). Each outgoing transaction has bulk and file reference as part of the payment details, which is available in the Payments Inquiry page. |
| Outward reversal generation | Generates pacs.007 at the end of clearing settlement cycle (configuration for each CSM and message type). Each CSM can have its own XSD and mapping requirements. Settlement transaction is created in the system for each bulk in the outgoing file. Settlement transaction accounting entries are as follows:   - Debit CSM suspense account - Credit CSM nostro account |
| Original collection marked as ‘Reversed’ | Marks the status of the original collection as ‘Reversed’, when processing of the outgoing DD reversal is successfully |
| Send customer status report | Sends the confirmation to customer in the agreed format (pain.002) and notifies about the reversals |
| Error queue | Parks the pain.007 batches failed due to message format in the Error queue. This can be viewed from the Received Files Enquiry page in TPH. The user cannot resubmit the file from this page, unless the failure is due to:  - Cannot determine the processing company ID - Acceptance configuration is not in the system |
| Repair queue | If the generation of outward pacs.007 payment fails in any component of TPH, the STP flow moves to the Repair queue for the user to repair or cancel the payment. The repaired payments continue with payment processing starting from debit account validations. |

## Inward Processing of SEPA DD from Clearing

This section describes the processing of an incoming DD from a SEPA clearing, initiated or sent by the creditor’s bank.



| Activity | Description |
| --- | --- |
| Message format validation | Validates pacs.003 message format by checking mandatory and non-mandatory fields, proper field length and content based on pacs.003 XML definition language file (provided by the clearing). |
| Mandate validation | Validates the mandate for B2B DD and amends it (when the amendment information is provided with DD and *Mandate Amendment* is enabled in the Clearing Setting configuration).  - In Core DD, the mandate validation is optional (according to the scheme) and auto-mandate creation can be activated. - If the mandate does not exist in DD.DDI, canceled, expired, or exceeds the limit (based on periodicity and maximum amount), the system routes the DD to repair or rejects it (automatically).  To know more, refer to Repair or Automated Reject processing. |
| Debit account validation | Validates the following for the debit account:  - Is a valid Temenos Transact Account. - If the account is invalid, frozen or closed, or does not exist, it routes the DD to repair or rejects it (automatically).  To know more, refer to Repair or Automated Reject processing. |
| Dates calculation | Determines the collection or settlement date (as the *RCLD* is from the inward DD).  - If the *RCLD* is equal to or before the current business date, the collection or settlement date is set equal to the current business date. - If the determined collection or settlement date is a bank holiday, the system forwards the date to the first banking business day based on the cut-off shift day. - To configure one day in channel cut-off, go to **Admin Menu**>**Payment Hub**>**Routing And Settlement**>**Channel Cut-off Configuration**.   Calculates the debit and credit value dates and book date, which equals the determined collection or settlement date. |
| Duplicate check | Enables to configure the check on the following:  - *End-To-End Reference* (Customer Specified Reference) - *RCLD* - *Mandate Reference* - *Creditor ID* - *Transaction Amount* - *Incoming Message Type*   The values of these fields can be changed or configured based on the client requirement.  If the duplicate check fails, the system routes the DD to repair or rejects it (automatically)  To know more, refer to Repair or Automated Reject Processing. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank specific requirement and is performed in the site. TPH solution is pre-integrated with Temenos FCM solution. During a HIT from filtering, it routes the DD to repair. |
| Warehouse future dated | - Warehouses DD initiations or schedules for release on the calculated debit value date (which is equal to settlement or collection date). - Validations (except bulk agreement and message format) are repeated on release. |
| Balance check | Checks whether sufficient funds are available in the debtor’s account before posting an inward DD. If sufficient funds are not available, it performs the following:  - Cancels or rejects the DD transaction automatically - Routes to the Repair queue - System can retry checking till the *RCLD* or settlement date. |
| Posting | Debits the debtor’s account with the transaction amount. If posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or rejects it. **Posting**   - Debit clearing suspense account is configured in Clearing Setting - Debit debtor is the client account   **Settlement Booking Entry**  If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Repair | Routes the inward DD with validation errors to the Repair queue for user intervention or rejects it (automatically). The user can repair the DD or reject it (manually) from the Repair queue. - Automatic reject processing is available only for TPH, which can be enabled using the clearing setting configuration. To know more, refer to Automated Reject Processing. - Automatic reject processing is performed when the following are not available:   - Debit account   - Mandate |
| Manual reject | Rejects the DD from the Repair queue (manually). System allows this only when the *Create Reject Message Indicator* field is configured in the Clearing Setting.   - To manually reject, go to **Admin Menu**>**Payment Hub**>**Local Clearing**>**Clearing Setting**. - In the *Error Information*, enter the reason code or description and then submit the DD from the Repair.   - The DD is authorised based on the authorisation principle. - The transaction can be rejected, when the current business date is before the settlement date or on the settlement date before the clearing reject cut-off time. |
| Automated reject processing | Rejects DD automatically when the *Automated**Return**Indicator* field is set as Y. Pre-condition –The current business date is before the settlement date or on the settlement date before the clearing reject cut-off time. |
| Original collection rejected | - Cancels DD and assigns status 998 (Rejected), when system rejects an inward DD (automatically or manually). - Updates the total bulk amount to be settled with the clearing at the determined settlement or collection date. |
| Generate and send pacs.002 message to clearing | Generates a pacs.002 reject message (or refusal message on behalf of the debtor) and sends it to clearing at the pre-defined clearing schedule. To know more, refer to Clearing Frequency configuration. |

## Inward Processing of SEPA DD Reject Messages from Debtor Bank



The status report message (pacs.003) has transaction information that is rejected or refused by a debtor for the corresponding original DD bulk (pacs.003) sent by a creditor bank.

| Activity | Description |
| --- | --- |
| Update status for the original outgoing DD bulk | Updates the status of the original DD bulk sent by the creditor bank to PART (partial), which indicates that an outgoing bulk has rejected transactions by the debtor bank. To view the status of the bulk, go to **User Menu**>**Payments**>**Payments Hub**>**Payment Inquiries**>**Received and Sent File Details**>**Sent File Details**. |
| Update amount to be settled for the original outgoing DD bulk | - Updates the pending settlement transaction of the original outgoing DD bulk, which is executed on a clearing settlement day (after reject cut-off time). - Books the settlement transaction with the total amount of the collections in the original pacs.003 bulk sent, minus the total amount of rejected transactions in the bulk. |
| Reject the original outgoing DD | Identifies and rejects the transactions based on the *Original Message ID* and *Original* *Transaction Reference* for each transaction in the pacs.002 message. If a rejected transaction is already booked (reject is received at the settlement date), the system generates a new reject transaction to refund the rejected amount. |
| Original collection marked as Returned | Marks the status of the original (returned) collection as ‘Rejected’ (998), after rejecting the incoming DD return. |

Reject messages with certain ISO reason codes can be routed to a manual ‘Reject’ or Clearing Status Report queue (if configured), which is not considered in this module.

## Inward Processing of SEPA DD Return or Refund from Clearing

This section describes the processing of an incoming DD return from a SEPA clearing, initiated or sent by the debtor’s bank, for the corresponding outgoing DD received from the creditor’s bank.



| Activity | Description |
| --- | --- |
| Message format validation | Validates pacs.004 message format by checking mandatory and non-mandatory fields, proper field length and content based on pacs.004 XML definition language file provided by clearing. |
| Debit account validation | Validates the following in a debit account:  - Is a valid Temenos Transact account - If invalid, frozen or closed, it routes the DD to repair |
| Dates calculation | Determines the credit value date as the inter-bank settlement date of the DD return (if pacs.003 bulk is available). If the inter-bank settlement date is a bank holiday, the credit value date is determined as the first banking business day (based on the cut-off shift day). To configure one day in channel cut-off, go to **Admin Menu**>**Payment Hub**>**Routing and Settlement**>**Channel Cut-off Configuration**. Based on the configuration, the debit value date is when the return payment is processed or equal to the *Original Interbank Settlement* *D**ate*. |
| Duplicate check | Enables to configure the checks based on the following:  - *End To End Reference* (customer specified reference) - *RCLD* - *Mandate Reference* - *Creditor ID* - *Transaction Amount* - *Incoming Message Type*  If the check fails, the system routes DD to repair or rejects it (automatically). To know more, refer to Repair or Automated Reject Processing. |
| Identify original payment | Identifies the original outgoing payment transaction based on the *Original Message ID* and *Original Transaction ID* in the incoming return or refund message. If the original transaction cannot be identified or not fully processed, it routes the return DD to the Repair queue. |
| Filtering | Performs filtering of payments when interfaced with a screening engine. This is a bank-specific requirement and is performed in the site.  TPH solution is pre-integrated with Temenos FCM solution. During a HIT from filtering, it routes the DD to repair. |
| Balance check | Checks whether sufficient funds are available on the debtor’s account before posting the debit return. If sufficient funds are not available, it performs the following:  - Routes the DD transaction to the Repair queue - System can retry checking till the settlement date. |
| Fees calculation | The received return has bank charges (interchange fees and compensation refund cost) for the R-message. These charges have to be paid to the original debtor bank. In TPH, these charges are debited from the customer (original creditor). The payment fails posting (debit side is not equal to credit side), when these charges are not setup for the product as client charges. |
| Posting | Debits the debtor’s account with the transaction amount. If posting fails (due to a posting restriction), it parks the payment in the Repair queue for user action or rejects it. **Posting**   - Debit clearing suspense account is configured in clearing setting - Debit debtor is the client account   **Settlement Booking Entry**  If SEPA payments are settled at the clearing settlement collection date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Original collection marked as ‘Returned’ | Marks the status of the original (returned) collection as Completed and Returned (996), when the incoming DD return is booked. |
| Repair | Routes the inward DD with validation errors to the Repair queue for manual intervention (repair). It does not allow return or reject of an inward DD return. |

## Inward Processing of Cancellation Request (camt.056)

Creditor bank can send cancellations (camt.056) to debtor bank through Equens CSM for DD collection (pacs.008) that is sent before the settlement date. The debtor bank cannot reject an incoming cancellation request.



| Activity | Description |
| --- | --- |
| Receive and map recall request | - Creditor bank initiates a cancellation request or at the customer’s (Creditor) requests before the last cut-off time for pre-settled R-messages - Debtor bank (TPH) receives the cancellation request for an already received collection request - Receives and maps the recall request in TPH - If the format validation of recall request message fails, it moves to the error folder |
| Create recall request | Creates a recall request record with ‘Inwork’ status to represent the cancellation request |
| Match with original payment | Matches the cancellation request with an existing inward direct collection request.  - If the original collection is found and not cancelled or reversed, the system checks whether the cancellation request can be processed immediately or requires manual intervention. If manual intervention is required, it moves the payment to Cancellation Request (CR) Manual queue. - If TPH does not find the original collection or the collection is either cancelled or reversed, it moves the recall request to Cancellation Request (CR) Manual queue for manual intervention. |
| STP CR processing | - Cancels the collection when the debtor is not debited for the collection and adjusts the settlement amount in the clearing pending settlement record for the pre-settlement R-message amount - Creates a reversal transaction when the debtor is already debited, where the original debtor is credited. If the settlement accounting with clearing is already raised (cancellation request is received after the reject cut-off time due to technical reasons), it reverses the settlement entries manually. |
| CR manual queue | User accepts or rejects the recall when the recall request is moved to Cancellation Request Manual queue based on previous activities. If accepted, processing takes place in STP CR processing. |
| Error | Moves the inward camt.056 to Error queue that fails due to format validations. The user can view this in the TP Received Files Enquiry page. |

## Inward Processing of SEPA DD Reversal (pacs.007)



| Activity | Description |
| --- | --- |
| Message format validation | Performs pacs.007 message format validation by checking the following:  - Mandatory and non-mandatory fields - Proper field length - Content based on pacs.007 XML definition language file (provided by the clearing) |
| De-bulking and mapping | Creates a reversal transaction (RV transaction type) for each record in the bulk and settlement transaction for the total amount (for each pacs.007 bulk in the file) |
| Credit account validation | - Validates whether the credit account (original debtor) is a valid account - Routes the reversal to Repair queue when the account is invalid, frozen or closed |
| Dates calculation | Receives the incoming DD reversals on the settlement date and settled on the same day with the clearing If settlement date is a non-working day for the processing bank, TPH bank that processes the reversal (if valid) credits the customer on the settlement date or next working day. Value date of the credit depends on the client conditions float agreement with the customer. |
| Duplicate check | Skips the duplicate check for return DD collections (if configured) |
| Identify original payment | Identifies the original outgoing payment transaction, based on the original message ID, original transaction amount, and original transaction ID available in the incoming reversal message |
| Sanction screening | Performs sanction screening of payments (if configured). This is a bank specific requirement and is performed in the site. TPH solution is pre-integrated with Temenos Financial Crime Mitigation (FCM) solution. This takes action (if configured) when there is a HIT from filtering. |
| Fees calculation | Reversed settlement amount in payment is the original transaction amount along with the bank charges (if any). The received reversal can have bank charges (optional) for the R-messages. Credits the charges paid by the sending bank to a profit and loss account (a revenue to the receiving bank ) |
| Posting | Raises the following accounting entries for an inward pacs.007 **Settlement entry (for each bulk)**   - Debit clearing nostro (value date is equal to settlement date in the file) - Credit suspense account (value date is equal to settlement date in the file)   **Individual Return Transaction**   - Debit clearing suspense account - Credit original debtor’s account |
| Original collection marked as reversed | - Marks the status of the original (reversed) collection as ‘Reversed’ when the incoming DD reversal is successfully processed - Reopens the mandate when the underlying collection is in the collection of a last or one-off mandate |
| Repair | Operator routes inward DD reversals with validation errors to the Repair queue for manual intervention. It does not allow return or reject of an inward DD reversal for SEPA.  The bank user performs the following actions in Repair queue:   - Modifies the transaction and resubmits it - Cancels the transaction in TPH |

## Inward Processing of Clearing Status Report (pacs.002)



| Activity | Description |
| --- | --- |
| PSR received from Equens CSM | Clearing (SDD) can perform the following:  - Reject any outward DD messages (pacs.003, pacs.004, pacs.007, pacs.002 (Refusal or Reject) or camt.056) against technical ) validations. - Receive a pacs.002 (clearing status report – SDD) after the validations (technical or functional).  Clearing Status Report is received from the clearing for the following outgoing messages:  - pacs.003 - pacs.004 - pacs.007 - pacs.002 (refusal or reject) - camt.056 |
| Process file level status | Parks the file in Sent Files Exception queue (when the full file is rejected) for the user to view. It does not allow the user to resubmit the file from this queue. The IT Operations team need to resubmission the files outside TPH. |
| Process bulk level status | - Creates reverse settlement transaction for all rejected amount (for each outgoing bulk) in a bulk. This applies to outgoing pacs.007 and pacs.004. In pacs.008, it adjusts the pending settlement record for the rejected amount. - Reverses and parks the rejected transactions in Exception queue (based on the configuration in the system) for user intervention. User can either resubmit the bulk or transaction to clearing and ignore or reverse the bulk or transaction in the system.  To perform automatic processing or when the user needs to select the reverse option from the Exception queue, the system does the following for a reject:  - pacs.004 and pacs.007 – Creates a new reversal transaction - pacs.008 – Cancels when the creditor is not credited or creates a reversal transaction when the creditor is already credited   It notifies the customer with a status report (if configured) in pain.002 for an outgoing Direct Debit (DD) collection.  - If a camt.056 is rejected, it marks the cancellation request as ‘CELEARINGREJECTED’ in the system. |
| Update outgoing message ACK Status | Marks the following acknowledgment and clearing statuses as follows:  - Acknowledgment status of the outgoing file as ‘Rejected’ (when the file is rejected) and clearing action status as pending for user intervention. - Acknowledgment status of the outgoing bulk as ‘Accepted’ (when the bulk is fully accepted). - As ‘Part’ (when partly accepted) and ‘Rejected’ (when fully rejected). - Clearing status as ‘Pending’ (when the bulk requires manual intervention and to view it from Exception queue). - Acknowledgment status of the outgoing message as ‘Rejected’ for each transaction that is rejected. - Clearing status as ‘Pending’ to view from Exception queue (when the transaction requires manual intervention). |
| Park PSR in exception queue | Views and takes actions on clearing status reports (validation and cancellation) that are parked in Sent Exception queue |

## Manual Return of Inward SEPA Payments



[Manual Return from the Repair Queue](#)

| Activity | Description |
| --- | --- |
| User initiates manual return or refund | Returns the DD from the Repair queue (manually), when:  - Inward SEPA direct debit cannot be booked on the settlement - Clearing cut-off time has already passed   - Direct debit is available or routed to the repair queue - Due to a posting restriction, closed or frozen account  To know more, refer to [Inward Processing of SEPA DD from Clearing](#Inward_Processing_of_SEPA_DD_from_Clearing). |
| User enters reason code or description in the Error Information tab and submit | Submits the DD from the Repair queue as ‘Returned’ with the reason code and description. Additionally, indicates whether the return is originated on behalf of the bank or debtor in the Error Information tab. The submitted transaction needs to be approved by another user from the Authorisation queue. |
| Timeline validation (acceptance days for returns) | Checks for maximum number of inter-bank business days allowed for a debtor bank to send return transaction after the settlement date of the original collection.  - B2B DD – 3 days - CORE DD – 5 days   This is configured in the Clearing Setting: Acceptance Days for Returns and the respective schemes. To know more, refer to [Configuration](../Europe_SEPA_Direct_Debit_PPSPDD/Configuration.htm) section.  - System checks the timeline, the user submits the return from the Repair queue and sends a warning (if it exceeds). - The timeline is validated again, when the user authorises the submitted return from the Repair queue. |
| Posting – inward SEPA DD | Debits the original amount of the incoming DD from a return suspense account (instead of the debtor’s account) and credits the clearing suspense account, when:  - User submits the DD from the Repair queue as ‘Returned’ - Another user approves the submitted transaction |
| Creates new DD return | A new SEPA DD return is created when the inward DD is booked. |
| Posting – DD return | A new SEPA DD return is created with the following posting:  - Credit return suspense account is configured in the Clearing Setting - Debit clearing’s suspense account is configured in the Clearing Setting   **Settlement Booking Entry**  If SEPA returns are settled at the clearing settlement date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. This happens when the return file is sent to the clearing as returns are pre-settled. |
| Original collection marked as Returned | If an outgoing DD return is booked, it marks the status of the original (incoming and returned) collection as Completed and Returned (996). |
| Generate pacs.004 message | Generates a pacs.004 return message (or Refund message when it is returned on behalf of the debtor) and sends it to clearing at the pre-defined clearing schedule. To know more, refer to Clearing Frequency configuration. |

[Manual Return, Refund from the Return or Refund Page](#)

| Activity | Description |
| --- | --- |
| User initiates manual return or refund | The Operator can manually refund the original direct debit, when:  - Inward SEPA DD is already booked on the settlement date - Debtor requests the debtor bank to refund its account with the original collection amount  Go to **User Menu**>**Payments**>**Payments Hub**>**Payment Investigations and Cancellations**>**Return/Reject Payments**>**Return/Reject Inward Direct Debits**. |
| System creates new DD return in OE page | If the user selects and confirms the original outgoing DD to be returned or refunded, then it creates a DD return or refund transaction (for which the reason code and description can be entered). |
| User enters reason code or description in the Error Information tab and submit | - Submits the DD from the Repair queue as Returned with the reason code and description. - Additionally, indicates whether the return is originated on behalf of the bank or debtor (return or refund) in the fields in the Error Information tab.   The submitted transaction needs to be approved by another user from the Authorisation queue. |
| Timeline validation (Acceptance days for returns) | Checks the maximum number of inter-bank business days a debtor bank is allowed to send a return transaction, after the settlement date of the original collection.  - B2B DD – 3 days - CORE DD – 5 days - Refunds (only CORE scheme):   - Authorised mandate - 8 weeks + 2 inter-bank business days   - Unauthorised mandate - 13 months   The number of days are configured in the Clearing Setting (To know more, refer to [Configuration](../Europe_SEPA_Direct_Debit_PPSPDD/Configuration.htm) section).  Checks the timeline when the user submits the return from the Repair queue and sends a warning (if the timeline exceeds).  The timeline is validated again when the user authorises the submitted return from the Repair queue. |
| Posting – inward SEPA DD | If a user submits the DD from the Return entry page as Returned, and another user approves and submits that the return is valid (time line), the following posting is applied:  - Credit return suspense account is configured in the Clearing Setting - Debit clearing’s suspense account is configured in the Clearing Setting   **Settlement Booking Entry**  If SEPA returns are settled at the clearing settlement date, the system creates and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account.  Debits the original amount of the incoming DD from a return suspense account (instead of the debtor’s account) and credits the clearing suspense account. |
| Posting – DD return | Creates a new SEPA DD return with following posting:  - Credit original debtor’s account - Debit clearing’s suspense account is configured in the Clearing Setting   **Settlement Booking Entry**  If SEPA returns are settled at the clearing settlement date, the system checks and posts a separate clearing settlement transaction to move funds between the clearing Nostro and suspense account. |
| Original collection marked as Returned | If an outgoing DD return is booked, it marks the status of the original (incoming and returned) collection as Completed and Returned (996). |
| Generate pacs.004 message | Generates a pacs.004 Return or Refund message (if returned on behalf of the debtor) and sends it to the clearing at the pre-defined clearing schedule. To know more, refer to Clearing Frequency configuration. |

A pacs.004 return message is sent to the respective SEPA clearing, when returns are initiated from the Manual Repair page, or returned or refunded from the Return or Refund page. Similar to outgoing DD, the system performs the reachability check and SEPA channel validations (if configured).

## Equens SEPA 2021 Direct Debits Rule Book Changes

The following functionalities are provided to cover the SEPA 2021 Rule Book updates for Equens CT and DD:

- Receive and process a bank request with a specific reason code, within the acceptance days configured for that reason code.
- The Additional Information tag has been made mandatory from optional, maximum 13 occurrences are allowed.
- Initiate and process a fee and interest compensation payment via a credit transfer request (pacs.008.001.02). A pacs.008 has been added for a payment of inter-PSP fee and/or interest compensation related to the inquiry messages camt.027/087.
- An enquiry on multiple credit transfer transactions is allowed.
- It possible to request only a fee (in charges) without necessarily an interest compensation (in compensation).
- Link Equens payments with preceding request-to-pay. RRTP is used in case the SCT is the result of a preceding request-to-pay message (RTP). EquensWorldline will accept and forward this code.
- The reject codes XT74 and XT75 are replaced with AG09 and RCON for both SCT and SDD.

## Equens SEPA Direct Debits 2023 Rule Book Changes

Equens RB change enables the migrating to 2019 version of the ISO 20022 and thus offer the end user the opportunity of using the features under the 2019 version which may not be available under earlier versions of the ISO 20022 standard.

- The existing version of the message identifiers is changed to newer version, therefore even the xsd should be replaced with the newer version in order to support the latest changes

  |  |  |
  | --- | --- |
  | Message older version | Message new version |
  | pacs.003.001.02 | pacs.003.001.08 |
  | pacs.002.001.03 | pacs.002.001.10 |
  | pacs.004.001.02 | pacs.004.001.09 |
  | pacs.007.001.02 | pacs.007.001.09 |
  | camt.056.001.01 | camt.056.001.08 |

- Reference ID's can now contain internal spaces however leading/trailing spaces are not allowed.
- The element “BIC” (2009 message version) changed to “BICFI” (2019 message version) and the element “BICOrBEI” (2009 message version) changed to “AnyBIC” (2019 message version).
- LEI is a new sub-element introduced under the organisation identification for debtor, ultimate debtor and ultimate creditor. When organisation identification is used either AnyBIC, LEI or One occurrence of Other must be present. Its is a 20-digit alphanumeric characters value.
- After the RB change 2023 payment end-users can benefit from the standard delivery of structured address details about the payer and the payee. It consists of Country and TownName(both mandatory) together with one or more of the other structured elements Department, SubDepartment, StreetName, BuildingNumber, BuildingName, Floor, PostBox, Room, PostCode, TownLocationName, DistrictName and CountrySubDivision. The user has the option to capture either Structured or Unstructured address. The current unstructured PostalAddress can be used in combination with country.
- Creditor reference information can be used to capture the remittance information and when used then the structure type and structure reference is mandatory.
- Original message name identification in the R messages now will contain the complete version of the original underlying message.
- Element Purpose is now present in the R messages and value must be present if it was present in the original message.
- New sub element party is introduced for all the party role tags - Debtor, Creditor, Ultimate Debtor, Ultimate Creditor. For example: Dbtr\_Nm changed to Dbtr\_Pty\_Nm.
- The element ChargesInformation sub-element Party is replaced by Agent. As a result, in the pacs.002 SDD Reject, the pacs.004 SDD Return/Refund and the pacs.007 SDD Reversal the sub element party will now be sent as agent. ChrgsInf\_Pty\_FinInstnId\_BIC changed to ChrgsInf\_Agt\_FinInstnId\_BICFI.
- The proprietary reasons codes TECH, FRAD in camt.056 are now moved under the ISO reason codes.

## Equens SDD Rulebook changes for 2025

The Equens Direct Debits (DD) clearing solution is fully compliant with the 2025 SEPA rulebook changes. Following are the key updates for Direct Debits, which are applicable for the pacs.003, pacs.004, camt.056, and pacs.007 message types:

- **Ultimate Debtor and Debtor<Org ID>**: For the SCT message types, the Organisation Identification sub-element under Ultimate Debtor and Debtor must include AnyBIC, LEI, and may contain one occurrence of ‘Other’.
- **Hybrid Postal Address Support**: Debtor and Creditor elements support Hybrid Postal Address. Town and Country are mandatory, and at least one address line is supported.
- **Allowed Days for Refund of Direct Debits**: To avoid rejections by other clearing houses, the SEPA-Clearer validates the R-transaction’s Interbank Settlement Date (ISD ) against the original transaction’s ISD. Below is the updated configuration:
  - Authorized refund: 47 TARGET days
  - Unauthorized refund: 310 TARGET days
  - Update these values in PP.CLEARING.SETTING table:
    - AuthRefundAllowedDays = 47
    - UnAuthRefundAllowedDays = 310
  - Record should have:
    - Direction = S
    - Incoming message type = pacs.003

In this topic

- [Introduction to Equens SEPA Direct Debit](#IntroductiontoEquensSEPADirectDebit)

- [Post and Pre-Settled](#PostandPreSettled)
- [SEPA DD Schemes](#SEPADDSchemes)
- [DD Batches versus Single DD](#DDBatchesversusSingleDD)
- [Recurrent and One-Off DD](#RecurrentandOneOffDD)
- [SDD Mandate Validation](#SDDMandateValidation)
- [Pre-Settlement SDD Events or Messages](#PreSettlementSDDEventsorMessages)
- [Post-Settlement SDD Events or Messages](#PostSettlementSDDEventsorMessages)
- [Bulking Criteria](#BulkingCriteria)
- [Outward Processing of DD Initiation (pacs.003)](#OutwardProcessingofDDInitiationpacs003)
- [Book Processing of DD Initiation](#BookProcessingofDDInitiation)
- [Outward Processing of Rejected DD (pacs.002)](#OutwardProcessingofRejectedDDpacs002)
- [Outgoing Processing of Cancellation Request (camt.056)](#OutgoingProcessingofCancellationRequestcamt056)
- [Outgoing Processing of Reversals (pacs.007)](#OutgoingProcessingofReversalspacs007)
- [Inward Processing of SEPA DD from Clearing](#InwardProcessingofSEPADDfromClearing)
- [Inward Processing of SEPA DD Reject Messages from Debtor Bank](#InwardProcessingofSEPADDRejectMessagesfromDebtorBank)
- [Inward Processing of SEPA DD Return or Refund from Clearing](#InwardProcessingofSEPADDReturnorRefundfromClearing)
- [Inward Processing of Cancellation Request (camt.056)](#InwardProcessingofCancellationRequestcamt056)
- [Inward Processing of SEPA DD Reversal (pacs.007)](#InwardProcessingofSEPADDReversalpacs007)
- [Inward Processing of Clearing Status Report (pacs.002)](#InwardProcessingofClearingStatusReportpacs002)
- [Manual Return of Inward SEPA Payments](#ManualReturnofInwardSEPAPayments)
- [Equens SEPA 2021 Direct Debits Rule Book Changes](#EquensSEPA2021DirectDebitsRuleBookChanges)
- [Equens SEPA Direct Debits 2023 Rule Book Changes](#EquensSEPADirectDebits2023RuleBookChanges)
- [Equens SDD Rulebook changes for 2025](#EquensSDDRulebookchangesfor2025)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:20:26 PM IST