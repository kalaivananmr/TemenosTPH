# Configuring SEPA Instant Clearing - EBA INST

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm) > Configuration

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
  - [Swiss Interbank Clearing Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
  - [SEPA Instant Clearing-EBA INST SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
    - [Introduction](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
    - [Configuration](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Configuration.htm)
    - [Working with](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Working_with.htm)
    - [Tasks](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Tasks.htm)
    - [Outputs](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Outputs.htm)
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
  - [Euro Swiss Interbank Clearing Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Configuring SEPA Instant Clearing - EBA INST

Updated On 10 July 2025 |
 17 Min(s) read

Feedback
Summarize

This section helps the user to understand the configuration of SEPA Instant Clearing.

## TPH as a Direct Participant (DP)

This section helps the user to understand the configuration of TPH as a DP in EBA Instant (EBA INST) Clearing.

[EBA INST Clearing](#)

In Model Bank (MB), TPH acts as a DP in the EBA INST Clearing. It can directly exchange messages with the EBA INST Clearing Channel (if configured). To configure EBA INST Clearing, perform the following:

- Define the EBA INST source.
- Define clearing (as a DP).
- Define the Message Type Level settings for clearing.
- Configure customer status reports to be sent at the correspondent bank and customer levels.
- Configure reports for EBA INST payments.

[Defining EBA INST Clearing as a Source](#)

TPH can receive payments from clearing. Hence, as a pre-requisite to clearing setting, define *Source* *Type* as NC (Non-client) in `PP.SOURCE` table.

- To define a source, go to **Admin Menu**>**Payments Hub**>**Static Data**>**Source**.



[Defining EBA INST as a Clearing Channel](#)

TPH can connect to the clearing channel as it is a DP to clearing.

1. To connect, go to **Admin Menu** > **Payments Hub** > **Local Clearing** > **Clearing**.




2. Define the following fields in the Clearing House of the PP.CLEARING table:

   | Field | Description |
   | --- | --- |
   | *Clearing Name* | Set as EBAINST |
   | *Participant Type* | If it is a clearing channel, then leave it blank. |
   | *File Transaction Ind* | If it is a single (not file) payment, set as T. |
   | *Clearing Type* | If it is an instant payment, set as I. |
   | *Clearing BIC* | BIC of the Clearing House to which the EBA INST payment is sent. |
   | *RTGS System* | If it is an instant channel, set as I. |
   | *Time Zone* | Time zone used while timestamping payments that are sent to clearing. [ClosedExample](#) EBA INST requires all payment initiations (to the Clearing House) to be timestamped with UTC time zone as the base. This is different from the time zone of the processing company (defined in the PP.COMPANY.PROPERTIES). |
   | *Target Execution Time* | Until when TPH can process outward instant payment after the Originator PSP has Time Stamped the Transaction (in seconds). |
   | *Posting Method* | The following values are available: - DebitNow – Reserves, books and sends the payment to the Clearing House. On confirmation from clearing, it marks the payment as completed or reverses the payment (based on positive or negative confirmation). - DebitOnPayConfirmation – Reserves and sends the payment to the Clearing House. On confirmation from clearing, it books the payment or cancels the reservation (based on positive or negative confirmation). |
   | *Inst Pay Rej Booking* | Action that system needs to perform when clearing sends a negative confirmation for an originated credit transfer (original transaction). The following values are available: - Reverse – This value performs the below functions:   - Sets status of original transaction to Rejected.   - Performs payment reversal.   - Reverses debit and credit amounts with charges applied.   - Does not calculate any new charges for the payment. - ReverseAndCharge – This value performs the below functions:   - Sets the status of original transaction to Rejected.   - Creates a new transaction reversing the debit and credit parties.   - Applies any charge configured for a new transaction   - Charges the customer for a negative confirmation from clearing. Any charges applied on the original payment remains the same. |
   | *Screening**Response**Action* | Behaviour of the system on receiving 'Possible Hit' response from the Filtering engine. |
   | *SendPendingConfirmation* | Sends a pending status confirmation message defined in the *Clearing Status Message Type* field (PP.CLEARING.SETTING table). EBA INST Clearing does not support the following options: - Reject – Sends a negative confirmation to clearing - Blank – No action required |
   | *Availability* | Has the following values: - 24/7 – Channel is available 24/7 for processing instant payments. System assumes that all days are working days, hence, does not perform holiday checks. - Blank – System is a non-24/7 channel for processing instant payment and checks for cut-off and holidays. |
   | *Clearing**Status**Message**Type* | Message type used when sending status confirmation to the Clearing House. - Can be positive, negative or interim confirmation. - A valid value in the PP.MSGPAYMENTTYPE |
   | *Ack**Type**Bene**ficiary* *Bank* | Defines whether the beneficiary bank expects the confirmation from clearing as: - TechnicalHandshake - Confirmation Message (not applicable for IPs) - On receiving an instant payment, it processes and sends the confirmation to clearing. - Beneficiary bank then expects a technical handshake through the interface layer for the confirmation message sent.  In some cases, clearing cannot support technical handshake and only sends a confirmation message (pacs.002). |
   | *Investigation Time* *Out**and* *Clearing Investigation Msg Type* | Time (in seconds) after which an automatic investigation (specified in the *Clearing Investigation Msg Type* field) is sent to clearing. |
   | *Investigation Retry Count* | Maximum number of times an investigation message can be resent when a confirmation for an originated payment is not received |
   | *Investigation Retry Time* | Time interval between sending automatic investigation messages |

[Message Types](#)

Define the following fields to configure the message types:

| Field | Description |
| --- | --- |
| *Clearing Transaction Type* | Helps to define the outgoing message in the associated *Outgoing**Message**Type* field. This needs to be a valid record in the PP.TRANSACTION.TYPES table`.` |
| *Out Message Format API* | It is mutually exclusive with the *Clearing Transaction Type* and *Outgoing Message Type* *fields*.  - If an API is defined to return the outgoing message type, system uses the API. - If API is not defined, it refers the associated multi-value set to find the outgoing message type. |
| *Outgoing Message Type* | Uses when sending the payment to the clearing house or DP. This needs to be a valid value in the PP.MSGPAYMENTTYPE table. |

[Defining the EBA Instant Clearing Settings Based on Message Type and Direction](#)

1. To define the clearing setting attributes, go to **Admin Menu** > **Payments Hub** > **Local Clearing** > **Clearing Setting**.


2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Max Inst Time Out* | Time (in seconds) within which the entire round trip of an instant payment needs to be completed |
   | *Auto Negative Cancel Req Response* | If an incoming cancellation request receives a negative response (original transaction not found or cancellation requests is beyond the allowed days), set the value as Y. This denotes that payment can be processed automatically without manual intervention |
   | *Original Trn LookUp Criteria API* | API used to retrieve the original transaction related to the incoming return, reversal or refund message. It differs based on clearing and clearing transaction types. If API is not defined, the above transaction types are not matched to the original transaction. |

## IP Channel for EBA INST Clearing when TPH is a DP

If TPH is a DP to clearing, it can receive payments from an IP and forward it to the EBA INST clearing. Similarly, TPH can receive payments from EBA INST clearing and forward it to IP. Hence, the IP channel and source need to be configured in TPH.

[Defining IP as the Source](#)

Define the *Source Type* field as NC (Non–client) in the `PP.SOURCE` table, as IP is a source from where payments are received.

Key to PP.SOURCE and PP.CLEARING tables are the same.



Key to the PP.CLEARING table needs to be an identifier for the IP. This can be a user defined name.



Set the *Participant Type* field as IP, which denotes it is an IP channel.

Automatic triggering of investigation messages does not apply for IPs.



[Defining the IP Channel Attributes](#)

- Define the IP channel attributes in the PP.CLEARING.SETTING table.

  The *Max* *Inst Time Out* field does not apply for IPs.
- Configure the *Negative Cancel Req Response* and *Original* *Transaction Returns* *API* fields.

## TPH as an IP

TPH as an IP in the EBA INST clearing can only connect to the DP. Hence, define DP as a channel in the PP.CLEARING table.

1. To define DP as a channel, go to **Admin Menu** > **Payments Hub** > **Local Clearing** > **Clearing**.
   Key to PP.SOURCE and PP.CLEARING tables are the same.


2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Channel Name* | Defines DP as a channel in PP.CLEARING table. - Name can be user defined. - A record with the same name needs to exist in the PP.SOURCE table. |
   | *Source Type* | DP is a source from where the payments are received. Set as NC (Non-client) in PP.SOURCE table. |
   | *Participant Type* | Denotes that TPH is connecting to a DP, when set as DP. |
   | *Clearing BIC or Clearing NCC* | Sends and receives payments from BIC or NCC of the DP. |
   | *Posting Method* | Allows to debit and send the payment to DP (as TPH is the IP), when set as DebitNow. |












## Customer Status Reports

[Correspondent Bank Conditions](#)

This table specifies the type of payment confirmation sent to the ordering customer for a correspondent bank (where TPH is a DP). The following are the configuration relating to confirmations:

- Whether ACK, NACK or BOTH are required.
- Whether an interim status report is required
  - If a correspondent bank sends a payment (which is forwarded to Clearing), then an interim status confirmation can be sent to the correspondent bank (if configured).
  - Once the payment reaches its final state (Completed or Cancelled), a final status confirmation is sent. This enables correspondent banks to know the status of their payments.

The *Message* *Type* (sent) is set as ACK or NACK.






[Client Conditions (Customer level configuration)](#)

Customer or account level agreements are available for instant payments. Hence, a default record is configured to hold the configuration. The following are the configurations relating to confirmations:

- Whether ACK, NACK or BOTH confirmations are required.
- Whether an interim status report is required
  - If a customer initiates a payment (which is forwarded to the Clearing), then an interim status confirmation is sent to the customer (if configured).
  - Once the payment reaches its final state (Completed or Cancelled), a final status confirmation is sent.

The *Message Type* (sent) is set as ACK or NACK.






To know more, refer to Status Reporting section.

## Reports Configuration for Instant Payments

[DRR](#)

1. To enable uploading of DRR file, configure EB.FILE.UPLOAD.TYPE application.



   Place the DRR file received in the appropriate path.


2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Hdr Upd Appl* | Name of the application to which the DRR file is loaded in PP.CLR.REPORTS.FILE |
   | *Hdr Upd Version* | Uses the version of PP.CLR.REPORTS.FILE,UPLOAD |
3. Configure EB.FILE.UPLOAD to upload the DRR file. After completion, authorise the record.
   File name needs to follow the standard convention: ExactFileName||FileSize||ExactFileName



To know more on generating the reports for instant payments in EBA INST clearing, refer to [Working with](Working_with.htm) section.

## Return and Reject Codes

EBAINST allows returning the settled original credit transfers based on the cancellation request received from the originating bank or creating the recall for the original credit transfer based on the EBAINST applicable return and reject codes.

To configure the reason codes,

1. Go to **Admin Menu** > **Payments** > **Payment Hub** > **Bank System Administration** > **Local Clearing** > **Clearing Return Code**.



2. Configure the following key fields as shown in above screenshot.

   | Field | Description |
   | --- | --- |
   | *CompanyID* | Indicates the company for which the record is created |
   | *ClearingID* | Specifies the name of the clearing maintained at TPH |
   | *ClearingReturnCode* | Indicates the reason code for initiating the recall request |
   | *ReturnCodeLevel* | Indicates the level for each clearing reason code defined:  - F – File based level - B – Bulk based level - T – Transaction based level |
   | *ReturnCodeDescription* | Describes the reason code given in the *ClearingReturnCode* field |
   | *ClearingTransactionType* | Defines the transaction type of the clearing |
   | *ClearingNatureCode* | Defines the code which identifies the nature of the clearing payment |
   | *ReturnAllowedDays* | Indicates the maximum days up to which recall can be initiated or recall request can be received. Format is as follows, where X is the number of days :  - X: X working days - XC: X calendar days - XW: X working days |
   | *Reason Code Type* | Indicates if the defined value of the *ClearingReturnCode* field is ISO or proprietary, based on the reason code |
   | *Bank Cust Initiated* | Indicates if request is initiated by bank or customer:  - B – Initiated by bank - C – Initiated by customer - \* – Applicable for both |

Read the [Configuring Manual Repair](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Manual_Repair/Configuration.htm) topic in the Manual Repair guide for more information on configuring return and reject codes.

## Cancellation Request by Bank

Read the [Configuring Manual Repair](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Manual_Repair/Configuration.htm) topic in the Manual Repair guide for more information on creation of cancellation request by the bank.

## Cancellation Request by Originator

Read the [Configuring Manual Repair](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Manual_Repair/Configuration.htm) topic in the Manual Repair guide for more information on creation of cancellation request by the originator.

## Qualifying LTA as Payment

When TPH receives a camt.054 message, it checks whether the transaction can be determined as LTA payment, based on the below configuration.

To configure the LTA qualification criteria, **Admin Menu** > **Payments** > **Liquidity Management** > **LTA Qualification**.

| Field | Description |
| --- | --- |
| Sending Institution Identification | Indicates the ID of the sending institution (RT1) |
| Receiving Institution Identification | Indicates the ID of the receiving institution (typically BIC of the bank) |
| Account Identification | Indicates the account of the participant whose liquidity position or balance has been adjusted. The value of this field can be,  - Bank identifier - Account Identifier (This is the account (RT1) where the user is a DP or liquidity serviced participant) |
| Advice Type | Indicates whether the LTA is for a debit or credit operation  - Debit indicator (DBIT) indicates debit on the user’s account (found in the *Debtor Account* field) - Credit indicator (CRDT) indicates credit on the user’s account (found in the *Credit Account* field) |
| Transfer Type | Indicates the type of the underlying Transfer. The value of this can be,  - Regular payment - Ancillary System (AS) transfer or liquidity adjustment |
| Local Instrument Proprietary | Indicates the proprietary type of the underlying transaction (for example, FICT) |
| CSM Status Code | Indicates the status of the adjustments as recorded within the RT1 system (for example, BOOK) |
| Debtor Agent | Indicates the agent who is debited. The value of this field can be,  - RT1 identifier (BIC) - User’s bank settlement BIC with the RT1 - Liquidity provider’s settlement BIC (depending upon the LTA being debited or credited) |
| Debtor Account | Indicates the account identifier of the debtor agent who is getting debited. The value of this field can be,  - RT1 account - User’s account with the RT1 - Any of the liquidity serviced participant’s account in case the bank provides such service (depending upon LTA being debited or credited) |
| Creditor Agent | Indicates the identifier of the agent who is credited. The value of this field can be,  - RT1 Identifier (BIC) - User’s bank settlement BIC with the RT1 - Bank’s liquidity provider’s settlement BIC (depending upon LTA being credit or debit) |
| Creditor Account | Indicates the account identifier of the creditor agent who is getting debited. The value of this field can be,  - RT1 account - User’s account with the RT1 - Any of the bank’s liquidity serviced participant’s account in case the bank provides such service (depending upon LTA being credited or debited) |

## Deriving Accounts for LTA Payment

If the LTA is qualified as a payment, the account for which the LTA notification is received is debited or credited in the receiving participant bank during LTA payment processing.

LTA payment comprises a debit and a credit account that represent accounts in which the liquidity adjustments were affected by the AHI. As the debit and credit accounts are external accounts to the bank, TPH resolves these accounts to an in-house Nostro or suspense account within the bank to perform necessary bookings. The posting is mainly for liquidity management purposes, such that receiving participant bank’s Nostro balances are up-to-date with the balance or positions in the actual account of RT1. This enables the receiving participant bank to perform efficient liquidity management functions.

The user can configure the in-house Nostro or suspense account in LTA Account Mapping application from following menu:

**Admin Menu** > **Payments** > **Liquidity Management** > **Account Mapping**.



In this topic

- [Configuring SEPA Instant Clearing - EBA INST](#ConfiguringSEPAInstantClearingEBAINST)

- [TPH as a Direct Participant (DP)](#TPHasaDirectParticipantDP)
- [IP Channel for EBA INST Clearing when TPH is a DP](#IPChannelforEBAINSTClearingwhenTPHisaDP)
- [TPH as an IP](#TPHasanIP)
- [Customer Status Reports](#CustomerStatusReports)
- [Reports Configuration for Instant Payments](#ReportsConfigurationforInstantPayments)
- [Return and Reject Codes](#ReturnandRejectCodes)
- [Cancellation Request by Bank](#CancellationRequestbyBank)
- [Cancellation Request by Originator](#CancellationRequestbyOriginator)
- [Qualifying LTA as Payment](#QualifyingLTAasPayment)
- [Deriving Accounts for LTA Payment](#DerivingAccountsforLTAPayment)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:19:31 PM IST