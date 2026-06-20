# Introduction to Nordic Instant Credit Transfer

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Nordic Instant Credit Transfer](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm) > Introduction

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
  - [Equens SEPA Credit Transfer Equens SEPA Credit Transfer](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Introduction.htm)
  - [TARGET2 Clearing (ISO20022) TARGET2 Clearing (ISO20022)](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Introduction.htm)
  - [Nordic Credit Transfer Payments Nordic Credit Transfer Payments](../../Europe/Europe_NCT_Payments_PPNPCT/Introduction.htm)
  - [Nordic Instant Credit Transfer Nordic Instant Credit Transfer](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm)
    - [Introduction](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm)
    - [Configuration](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Configuration.htm)
    - [Working with](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Working_with.htm)
    - [Tasks](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Tasks.htm)
    - [Outputs](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Outputs.htm)
  - [Euro Swiss Interbank Clearing Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Introduction to Nordic Instant Credit Transfer

Updated On 22 March 2025 |
 31 Min(s) read

Feedback
Summarize

The Nordic Credit Transfer (NCT) is a payment instrument used for transferring funds between two payment accounts (sending and receiving) held by banks located within the Nordic countries. The business and technical requirements of the NCT instant are defined and managed by the Nordic Payments Council (NPC) based on (but not limited to) the Single Euro Payments Area (SEPA) payment schemes. It also allows to develop and manage additional schemes and rules with participants, national communities and regulating authorities (in documents, such as rulebooks, the implementation guidelines and other publications).

## Type of Participants

The Source, Channel and Clearing settings can be defined separately based on whether TPH is a DP or IP in the Nordic Instant Clearing scheme (as it supports both). To know more, refer to [Configuration](Configuration.htm) section.

## Time Stamping of Instant Payments

This is an important feature of instant payments and is done before the payment is released to Nordic Instant Clearing.

- If the instant payment is received within the configured time out limit, the timestamp is validated and processed.
- If it is not received within the configured timeout limit, the payment is rejected back to the clearing.

Calculates the timestamp once, which remains unchanged in the entire payment roundtrip in the Nordic Instant Clearing.

## Dates

TPH does not perform channel cut-off or holiday checks (for example, clearing, currency and country holiday checks) on instant payments, as Nordic Instant is a 24\*7 channel. However, the Debit Value Date (DVD) and Credit Value Date (CVD) can be determined for the instant payment based on the Requested Execution Date from a pain.001 or Requested Credit Value Date (RCVD) from an incoming pacs.008. To know more, refer to [Business Dates](../../Payments_Hub_(PP)/Business_Dates/Introduction.htm).

## Currency

Nordic Payment Council (NPC) instant CT allows more than one currency unlike the EPC SEPA. The scheme covers currencies such as Danish Krone (DKK) and Swedish Krone (SEK), also known as scheme currencies.

## Routing

If the criteria for Nordic instant payments is not met, TPH routes the payment to other suitable instant payment channels in that geography.

An instant payment processed in the Netherlands (NL) can be routed through Nordic Instant and NL clearing. Hence, the system can route to multiple instant payment channels based on rules.

If the transaction amount is more than 15,000 EUR, the payment is routed through the NL instant scheme (as the Nordic instant scheme has a transaction limit of 15,000 EUR). In addition, some instant payment schemes can have a cut-off time (not 24\*7). If the cut-off time is missed, the system routes through another instant payment scheme (as configured) in TPH. To know more, refer to [Routing and Settlement](../../Payments_Hub_(PP)/Routing_and_Settlement/Introduction.htm).

## Charges

Charge types are mapped to SHA for instant payments in TPH.

Standard TPH charge calculation logic applies to instant payments.

## Maximum Amount

According to NPC scheme currency, the maximum amount is set at separate levels for single NCT instant transaction. The maximum amount for DEK is 500,000 (DEK) and SEK is 1,000,000 (SEK).

## Clearing Directory and Reachability

P27 NPC Instant scheme has no published clearing directory specification. Participants commit to another participate in the scheme as one of the following:

- Beneficiary Bank
- Both originator bank and beneficiary bank

The participate needs to commit to process the NCT instant transactions, according to the rules of the scheme. All participants need to be reachable domestically in one of the scheme currencies with the option to accept cross-border NCT instant transactions (currencies they adhere).

## Manual Entry of NPC Instant Payments

The user can manually enter Nordic instant payments by using the Instant Payment Order page. To know more, refer to [Working with](Working_with.htm) section.

## Investigations

This enables the originator bank to send an inquiry message to clearing, when response is not received from the Instant Payment Clearing after the time out deadline. Clearing can respond to the inquiry or investigation with a positive or negative confirmation (rejection). If the beneficiary bank confirms that funds are available to the beneficiary and instant payment transactions are successful, then clearing responds with a positive confirmation (which comprises of the following):

- Inquire status of instant payment order
- Originator bank can trigger the investigation message
- Beneficiary can receive investigation from CSM
- Trigger investigation on list of unconfirmed instant payments

## Recalling an NPC Instant Payment

[Originator Bank](#)

In Nordic Instant Payment Clearing, the originator bank participant can perform the following:

- Requests to recall a previously settled instant payment transaction within the prescribed deadline that follows the interbank settlement date.
- Sends the payment cancellation request based on the request from the originator or on its own.
- Receives the recall request from an IP (addressable), which it can record and forward to the clearing.
- Initiates a recall for one of the following reasons:

- Duplicate payment sent
- Technical problems that results in erroneous instant payment transaction
- Fraudulent originated instant payment

Recall needs to be initiated within 10 working days of the original instant payment transaction inter-bank settlement date. If the originator initiates a recall of an instant payment for reasons other than the above, the originator bank:

- Needs to accept the requests within 13 months from the debit date of the original instant transaction.
- Is not obliged to guarantee return of funds and needs to inform the originator.

If the recall is within the prescribed number of days (10 business days for originator bank recall and 13 months for originator) of execution of the initial instant payment transaction, the originator bank participant sends a Payment Cancellation Request (camt.056) message to the beneficiary bank.

The beneficiary bank can do one of the following:

- Accept the payment recall request and return the funds by sending a Payment Return message (pacs.004)
- Refuse the payment recall request and send a Resolution of Investigation (ROI – camt.029 message)

If the beneficiary bank responds within the prescribed period (10 business days following the receipt of the recall message), the originator bank supports the following:

| Response | Description |
| --- | --- |
| Accepts the cancellation request and sends a payment return | - Processes the incoming return payment (pacs.004) and credits the originator or IP bank account (serviced by the DP) or forwards it to the IP bank (if applicable). - Updates the status of the Payment Cancellation request and records the positive resolution of the cancellation request (that is, updates the details of the payment return message or transaction). - Relays status to the originator according to the agreed terms and forwards the Payment Return message to IP. |
| Sends a negative answer (that is Resolution of Investigation message), as a response to the cancellation request | - Updates the status of the Payment Cancellation request and records the negative resolution of the cancellation request (that is, updates the details of ROI received including the reason for rejection). - Relays status to the originator or IP according to the agreed terms and conditions. |

[Beneficiary Bank](#)

The originator bank participant in the Instant Payment Clearing can request recall of a previously settled instant payment transaction within the prescribed number of days following the interbank settlement date. Instant payment clearing forwards the payment cancellation request to the beneficiary bank participant.

Nordic instant in the beneficiary bank supports the following workflow when the payment cancellation request is received:

1. Verify whether the payment cancellation is received within the prescribed time limit.
2. Notify beneficiary of the payment cancellation request and get consent for returning the money.
3. If the recall is against an instant payment of an IP (addressable) serviced by the receiving beneficiary bank, it records the recall and forwards the payment cancellation request to the beneficiary bank.
4. If the beneficiary agrees to return the payment, then perform the following to recall it:
   - Create a new return payment and send to the clearing
   - Update the payment cancellation request as Closed, after updating the return payment details.
     The system supports generation of ISO20022 pacs.004 payment return message.
5. If the beneficiary does not provide consent to return the payment, send a negative answer to the originator bank through clearing.
   - Generate an ROI message (camt.029)
   - Update the payment cancellation request as Closed, after updating the details of the ROI.
6. Forward recalls to the IP (addressable) beneficiary bank, the DP bank can receive the positive (pacs.004) or negative confirmation (camt.029) and forward it to the clearing.

## Bank Identifier Code (BIC) and IBAN

The preferred bank or branch and beneficiary account identification methods used in Nordic clearing are International Bank Account Number (IBAN) and BIC, respectively. According to Nordic clearing regulation, NCT instant payment (pain.001) initiated by the customer can come without the beneficiary BIC. The beneficiary BIC is derived from the beneficiary IBAN.

## Initiating NCT Instant

NCT Instant can be initiated using the following:

|  |  |
| --- | --- |
| pain001 | System supports payment initiation through pain.001. It can result in book (beneficiary in the books of the processing bank) or outward transfer (pacs.008 is sent to clearing). |
| Payment Order | - User needs to input ordering and beneficiary customer details, payment amount, payment currency, requested execution date or requested credit value date calculated based on payment order product configuration, which is validated and committed. - Authoriser approves the payment order, and the system processes it as a book or an outward payment depending on where the beneficiary resides. The pacs.008 message is sent to clearing for outward payments. |

## Requesting for Status Update (pacs.028)

The ordering bank can send a request for status update (pacs.028) for camt.56 and the beneficiary bank can receive and process it. Additionally, it can send a request to the beneficiary bank for status update of an inquiry for which they have not received any response. This message is optional and is sent to the beneficiary bank, when the originator bank has not received:

- An answer to a Recall (camt.056) of an NPC instant
- A confirmation (positive or negative) five seconds after the time-out deadline

When the beneficiary bank receives a request for status update (pacs.028), it performs the following:

- If the recall request is already accepted, it generates (interbank return credit transfer message - pacs.004) with the original accept reason code as response
- If the recall request is already rejected (that is, a camt.029 is sent to the originator bank), it generates a camt.029 (negative response) with the original reject reason code as a response.

## Outward Processing of Payment Request (pacs.008)

Payment can be initiated from Payment Order or through a pain.001 file (message initiated by customer). The below diagram shows the processing activities involved in the payment flow in sequence.



| Activity | Description |
| --- | --- |
| Manual capture of NCT instant payment from branch or back-office using `PO` application or Order Entry (OE) page | Captures an NCT instant payment from PO application or TPH. Validates mandatory and non-mandatory fields on submission and displays errors (if any). |
| Payment instructions through customer channels or PISP | Sends the NCT instant instruction to TPH bank using customer channels (internet or mobile) or through intermediary service provider PISP and receives it as pain.001 message. |
| Account validations | Validates ordering or debit account has posting restrictions and has sufficient balance to cover the transaction. It checks whether the debit account has sufficient funds to process the transaction. |
| Debit or credit bank validations | Validates whether the beneficiary bank BIC or IBAN code is valid by validating the BIC against NCT instant payment directory (if this directory is loaded, system validates it against BIC or IBAN from the directory). It also performs the following validations:  - Populates either 'IBAN’ or ‘Other’ - NPC schemes use IBAN to define a beneficiary account |
| Business validations | NPC scheme adhere to any or both ‘SEK or DKK’ currency. Participants in the NPC schemes opt to receive cross-border payments. NCT instant payment clearing system is designed to be multi-currency and provide settlement in SEK or DKK. |
| Balance reservation | Validates whether ordering or debit account has posting restrictions and sufficient balance to cover the transaction. It also checks whether the Debit Account has sufficient funds to process the transaction. |
| Submission and supervisor approval | Performs the following validations:  - On submission of the payment, it waits for Supervisor’s approval. - Once approved, it is moved for further processing.  If rejected, it is modified and resubmitted for approval. It is then sent to Temenos Payments Hub Engine for further processing. |
| Warehouse | Warehouses payment with future execution date and releases it on the Start of Day (SOD) of the execution date. |
| Filtering | Performs filtering of payments when interfaced to a screening engine. This is bank specific requirement and is undertaken at onsite. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Routing | Routes payment to a TPH clearing channel ‘NCT Instant Clearing – CSM. |
| Dates calculation | Calculates the payment value date (if configuration) based on Requested Credit Date or Requested Execution Date. |
| AMS balance reservation | Reserves funds on the debit account. Balance reservation is done on Payment amount along with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode - If the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| FX or charge calculation | Calculates the cross-currency exchange rate when customer account and beneficiary account currency are different.  The beneficiary bank can reject the transaction when the payment amount is in a different currency of the beneficiary’s account. Charge mode is set as Shared ( ) for NCT instant payments. TPH calculates the applicable charges (if configured) |
| Posting | Debits the debtor’s account with payment amount and any charges to be borne by the customer. If posting fails due to insufficient funds for an instant payment after account validation and after receiving confirmation from clearing, it parks the payment in special queue for manual intervention  - If Account Management System (AMS) is Temenos Transact, then TPH performs debit posting in embedded mode - If the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  Outgoing Payments – Entries made before sending pacs.008 to clearing  - Debit debtor account - Credit NCT instant clearing suspense account |
| NCT instant channel validations | Performs specific validations on the payment to meet the compliance requirements of NPC clearing. |
| Time stamping the payment | Time stamps NCT instant payment before sending to clearing. |
| Outgoing payment generation | Generates all NCT instant payments (pacs.008) which is time stamped before sending to the clearing system. |
| Error queue or payment cancellation | If an error occurs while processing NCT instant payment, it cancels the transaction automatically. |

## Inward Processing of Payment Request (pacs.008)



| Activity | Description |
| --- | --- |
| NCT Instant Payment is Received from CSM or from DP | Receives an incoming payment (pacs.008) from CSM and changes it to neutral credit transfer format in TPH. |
| NCT Instant Payment specific format validations | Validates whether NCT instant payment is received (according to the message specification) and time stamped. |
| Instant Time Stamp Validation | When a payment is received from the CSM, TPH validates acceptance date time stamp on the payment. The time stamp is checked only when TPH is a DP, and receiving the payment from clearing to either credit a beneficiary in book or forward it to IP. Do not modify the time stamp and NCT instant payment redirect to other intermediary banks. |
| Credit Account Validation | Validates the beneficiary account for the following:  - Beneficiary bank BIC or IBAN unknown - Beneficiary account closed, dormant or stopped - Account is not in currency quoted - NPC schemes use IBAN to define a beneficiary account. The identification code consists of two elements: Scheme Identifier and Other Identification |
| Bank Code Validation | Validates creditor BIC when the originator bank explicitly requests the BIC of the beneficiary bank, where one of the two banks is located in a non-EEA SEPA country or territory. |
| Dates Calculation | Calculates credit value date received in the NCT instant payment. |
| Filtering | Filters the payments (if configured). This is a bank specific requirement and is performed in the site. |
| FX/Charge Calculation | Calculates the applicable charges according to the sharing principle. Charge mode is set as Shared ( ) for NCT instant payments. |
| Credit Posting | Performs posting as follows:  - Credit – Beneficiary account - Debit – Clearing suspense account |
| Error Queue | If an error occurs when processing NCT instant payment, it requires manual intervention to repair or cancel the payment. When the system cancels the transaction, it sends a negative confirmation to clearing. |

## Outward Request for Recall (camt.056)

TPH can receive an incoming interbank positive response (pacs.004) or interbank negative response (camt.029) for the Outgoing Recall Request (camt.056).



| Activity | Description |
| --- | --- |
| Create Cancellation Request (EBQA Screen) | Bank Operator initiates a recall request (for an outgoing pacs.008 already sent) either as bank or customer-initiated recall request.  - In bank-initiated recalls, the bank operator selects ISO reason codes (DUPL) or proprietary reason codes (TECH, FRAD) - In customer-initiated recalls, the bank operator selects either ISO reason code (CUST) or proprietary reason codes (AC03, AM09) |
| Validate Cancel Acceptance days | Validates whether a cancellation request is made for a payment within defined acceptance days. If cancellation request crosses the acceptance days, the system raises an error to the bank operator. |
| Authorise Cancellation Request (EBQA screen) | Supervisor authorises the recall. |
| Generate camt.056 | Generates and sends the cancellation request (camt.056) to clearing. |
| Error Queue | If there is a validation failure while processing Request for Recall, system displays an error to the bank user. |

[](#)[Incoming Interbank Positive Response (pacs.004)](#)



| Activity | Description |
| --- | --- |
| NCT instant payment recall request received from clearing or DP | Receives an incoming payment (pacs.004) from clearing and transforms it to neutral format in TPH. |
| Account validation | Validates the beneficiary account for the following:  - Beneficiary BIC, IBAN or account number unknown - Beneficiary account closed - Beneficiary account stopped - Account is not in currency quoted |
| Match incoming return with original outgoing camt.056 request | Checks whether there is any associated recall request for the pacs.004 message received. If associated recall request is found, system:  - Marks recall request as ‘Return Inprogress’ - Parks payment for posting confirmation (if configured) - Marks the original payment (pacs.008) status as ‘Payment is being Returned’. - Creates a new return payment |
| Credit validation | Validates the creditor BIC or IBAN, if the payment is destined for an indirect participant. |
| Value date calculation | Processes the returns on the same day it is received |
| Fee processing | Enables fee component in TPH for fee processing and fee collection is based on the configuration. |
| Duplicate check | Performs duplicate check on payments received from NPC clearing for the configured set of payment attributes, such as payment amount, currency and transaction reference. |
| Credit posting | Credits the payer account as part of new return payment. |
| Mark recall request and original payment status | Received pacs.004 for outgoing camt.056  - Marks recall request as ‘Cancel Accepted’ (Post confirmation from clearing, if configured) - Updates original payment as ‘Payment Completed with Return’ |
| Error queue | If the validation of pacs.004 message format fails, system moves the return payment to Error queue. |
| Repair queue | - If return payment processing fails during business validations or matching with original payment, then system moves the return payment to Repair queue for manual action. User can accept or reject the return payment. - If return payment is repaired, it starts processing from business validations. |
| Customer notification | Bank can configure TPH to send notification to customer (according to client specific requirements). |

[](#)[Incoming Interbank Negative Response (camt.029)](#)



| Activity | Description |
| --- | --- |
| Receive and map | When TPH (beneficiary bank) receives an Incoming Recall Response (camt.029) for the Recall Request (camt.056) from Clearing, it is transformed to neutral format. If validation fails, TPH moves camt.029 to the Error queue |
| Match to recall request | TPH matches the recall request with received recall response:  - If a match is found, TPH validates the recall request status - If the match is not found, TPH ignores the Recall Response (camt.029) and moves it to the Error queue |
| Validate recall status | - If recall request status is ‘CANCEL SENT’, then TPH validates the Cancellation Overdue days. - If recall request status is greater than or lesser than ‘CANCEL SENT’, it ignores the further recall response. |
| Validate overdue days | If the recall response is received within defined period (cancellation overdue days), the system accepts the recall response. |
| Update recall request status | If recall interbank negative response is accepted, system marks the status as ‘Cancel Rejected’ |

## Inward Request for Recall (camt.056)

The originator bank sends cancellation request to beneficiary bank through NPC clearing for the previously settled pacs.008 message. The beneficiary bank can respond with outgoing interbank positive response (pacs.004) or negative response (camt.029).



| Activity | Description |
| --- | --- |
| Recall request is received from the CSM clearing or from DP | Cancellation requests are initiated either by originator bank or customer (payer). TPH (Beneficiary bank) receives this request for an already received payment.  If recall request message format validation fails, it is moved to the error folder. |
| Duplicate check | Checks if the recall request is already received and then the status. If recall request is found and it is in the following status:  - Cancel Accepted – System sends negative response (camt.029) to payer bank - Rejected – System moves the duplicate recall request to Repair queue for manual action |
| Create recall request | Creates a Recall Request record with ‘INWORK’ status to represent the cancellation request |
| Match with original payment | Tries to match the cancellation request with an existing incoming payment request.  - If the original payment is found, system validates whether the recall request is received within defined period (configurable). - If original payment is not found, it moves the recall request to Repair queue for manual action or rejects automatically (based on configuration).  The following are the matching conditions:  - Transaction amount - Settlement date - Original transaction ID |
| Validate acceptance days | Validates whether the recall request is arrived within acceptable days (configurable).  - If bank initiates the recall, it invokes ‘Return Flow’ (can be due to duplicate ‘DUPL’ or fraud ‘FRAD’). - If customer initiates the recall, it moves them to Repair queue for manual action.   User can accept or reject the recall request. If recall request is not received within the defined period, it moves the request to Manual queue for user action or rejects automatically (based on the configuration). |
| Invoke return flow | If request is found valid, TPH invokes return processing. To know more, refer to [Outgoing Interbank Positive Response](#Outgoing_Interbank_Positive_Response_(pacs.004)) section. |
| Go to outgoing camt.29 flow | To know about outgoing camt.029 flow, refer to [Outgoing Interbank Negative Response](#Outgoing_Interbank_Negative_(camt.029)) section. |
| Error | If an error occurs in recall requests, TPH generates camt.029 automatically. |
| Repair | When the recall request is moved to Repair queue based on previous activities (refer Error), the user needs to perform one of the following:  - If accepted, recall processing continues. - If rejected, TPH generates camt.029. To know more, refer to Manual Recall section. |

[](#)[Outgoing Interbank Positive Response (pacs.004)](#)

TPH initiates return processing in one of the following scenarios:

- Recall request is received and beneficiary bank confirms the payment is returned
- Received credit transfer cannot be processed due to errors
- Beneficiary (customer) requests to return the payment



| Activity | Description |
| --- | --- |
| Map and create return record | Creates a return record by mapping payment data from original credit transfer (pacs.008).  - The Beneficiary party becomes the ordering party of the original transaction - The Ordering party becomes the beneficiary party of the original transaction - The debit main account is in the client account (as the beneficiary party of the original transaction is credited when the incoming transaction is processed) - The credit main account is an outgoing suspense account related to the originating channel  If mapping fails, it marks the return record as an error. The return record can be viewed in TPH using Transaction Type as RT. |
| Credit account validations | Validates whether the credit account has no posting restrictions and sufficient balance to cover the return transaction. |
| Balance reservation | Reserves fund on the debit account (Original credit account). Balance reservation is done on payment amount with charges.  - If Account Management System (AMS) is Temenos Transact, then TPH performs funds reservation in embedded mode. - If AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Date calculation | Calculates the return payment value date and booking date configured to current date (same as execution date) To return the positive answer (output message) sent within the configured days to the date of cancellation request. A separate time scheduled process creates settlement transaction for outgoing return credits. |
| Routing | Routes the return payment to a TPH clearing channel (same as original payment clearing channel) ‘NCT Instant Clearing’, which is configured for sending it to return NCT instant payment. Clearing channel can determine the return message type (pacs.004) |
| Charge calculation | Calculates the applicable charges for positive answer to recall pacs.004 (according to the configuration) |
| Filtering | Filters the payment when interfaced to a screening engine. This is a bank specific requirement and is performed in the site. Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Debit posting | Generates the following booking during the processing of the return (as positive answer to a recall or cancellation request):  - Debit – Client account (original amount) - Credit – Outward clearing suspense account - Credit – P&L account (any Return charges) Original amount – return charges  If the return transaction is successfully booked, it updates the status to ‘Pending to be sent to the Clearing’ in the system. A separate time scheduled process creates settlement transactions for outgoing return credits. |
| Outward interbank positive response | Generates outgoing pacs.004 message |
| Error queue | If validation of pacs.004 message format fails, it moves the request to Error queue. |
| Repair queue | If outgoing pacs.004 payment generation fails in debit account validations, reachability check, balance reservation, filtering, cut-off validations, channel validations, the return payments moves to Repair queue for manual action.  - If user repairs the return payment, then return payment processing starts again from debit account validations. - If user rejects the return payment in Repair queue, then negative camt.029 is sent to NPC clearing. |

[](#)[Outgoing Interbank Negative Response (camt.029)](#)



| Activity | Description |
| --- | --- |
| Recall request in manual repair queue | Handles incoming recall requests (manually) by moving them into Repair queue based on configuration (that is, auto-negative cancel request response is disabled) |
| Reject recall request | Bank operator can reject the recall request based on customer consent |
| Recall status updated | If recall request is rejected, it updates the EBQA status to indicate the rejection |
| Generate camt.029 | - If recall request is responded with a rejection, it generates a negative response (camt.029) automatically and sends them to NCT instant payment clearing. - If recall request is not responded within the configured overdue days, it generates negative response (camt.029) automatically and sends them to NCT instant payment clearing. |

## Request for Status Update (pacs.028)



| Activity | Description |
| --- | --- |
| Overdue days breached | Bank user manually initiates ‘Request for Status Update’ message (pacs.028) for the cancellation request (camt.056) sent by the originator or originating bank |
| Recall response received from CSM Clearing | Follows one of the following processes based on the response received from the beneficiary bank:  - [Incoming Interbank Positive Response (pacs.004)](#Incoming_Interbank_Positive_Response_(pacs.004)) workflow - [Incoming Interbank Negative Response (camt.029)](#Incoming_Interbank_Negative_Response_(camt.029)) workflow |

## Outward Investigation (pacs.028)



| Activity | Description |
| --- | --- |
| Investigation time out expired | TPH does not receive pacs.002 status response message from the beneficiary bank after the time out limit.  - TPH generates automatic investigation message (pacs.028) based on the configuration - Bank user manually initiate investigation message from the enquiry |

## Inward Payment Status Response (pacs.002)

The originator bank receives payment status response (pacs.002) for pacs.008 from the beneficiary bank.



| Activity | Description |
| --- | --- |
| PSR received from NPC clearing | Originator bank receives payment status response for pacs.008 from the beneficiary bank:  - Positive confirmation message with status code as ACCP - Negative confirmation message with status code as RJCT |
| Match with original payment | Based on the matching criteria, pacs.002 is automatically matched with the original payment message (pacs.008) in TPH |
| Update payment status | If original payment is found and status is ‘Accepted’ or ‘Rejected’, then TPH marks the original payment automatically as ‘Completed’ or ‘Rejected’, respectively |
| Update investigation status | If the original message ID is pacs.028, then pacs.002 is a negative confirmation from clearing and updates the Investigation status in TPH as ‘REJECTED’ |

In this topic

- [Introduction to Nordic Instant Credit Transfer](#IntroductiontoNordicInstantCreditTransfer)

- [Type of Participants](#TypeofParticipants)
- [Time Stamping of Instant Payments](#TimeStampingofInstantPayments)
- [Dates](#Dates)
- [Currency](#Currency)
- [Routing](#Routing)
- [Charges](#Charges)
- [Maximum Amount](#MaximumAmount)
- [Clearing Directory and Reachability](#ClearingDirectoryandReachability)
- [Manual Entry of NPC Instant Payments](#ManualEntryofNPCInstantPayments)
- [Investigations](#Investigations)
- [Recalling an NPC Instant Payment](#RecallinganNPCInstantPayment)
- [Bank Identifier Code (BIC) and IBAN](#BankIdentifierCodeBICandIBAN)
- [Initiating NCT Instant](#InitiatingNCTInstant)
- [Requesting for Status Update (pacs.028)](#RequestingforStatusUpdatepacs028)
- [Outward Processing of Payment Request (pacs.008)](#OutwardProcessingofPaymentRequestpacs008)
- [Inward Processing of Payment Request (pacs.008)](#InwardProcessingofPaymentRequestpacs008)
- [Outward Request for Recall (camt.056)](#OutwardRequestforRecallcamt056)
- [Inward Request for Recall (camt.056)](#InwardRequestforRecallcamt056)
- [Request for Status Update (pacs.028)](#RequestforStatusUpdatepacs028)
- [Outward Investigation (pacs.028)](#OutwardInvestigationpacs028)
- [Inward Payment Status Response (pacs.002)](#InwardPaymentStatusResponsepacs002)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:21:02 PM IST