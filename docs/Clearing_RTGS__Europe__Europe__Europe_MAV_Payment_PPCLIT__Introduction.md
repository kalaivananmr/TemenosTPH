# Introduction to Mediante Avviso (MAV) Payment

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_MAV_Payment_PPCLIT/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [MAV Payments](../../Europe/Europe_MAV_Payment_PPCLIT/Introduction.htm) > Introduction

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
    - [Introduction](../../Europe/Europe_MAV_Payment_PPCLIT/Introduction.htm)
    - [Configuration](../../Europe/Europe_MAV_Payment_PPCLIT/Configuring.htm)
    - [Working with](../../Europe/Europe_MAV_Payment_PPCLIT/Working_with.htm)
    - [Tasks](../../Europe/Europe_MAV_Payment_PPCLIT/Tasks.htm)
    - [Outputs](../../Europe/Europe_MAV_Payment_PPCLIT/Outputs.htm)
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

# Introduction to Mediante Avviso (MAV) Payment

Updated On 11 March 2021 |
 4 Min(s) read

Feedback
Summarize

The Mediante Avviso (also known as ‘Payment through Notice) is a paper notification that a creditor bank sends to the creditor to collect payments from the debtor. It has the necessary information of the creditor's (receiving) bank, and creditor for the reconciliation of the payment. This information is sent to the debtor to make the payment. Once the payment is received, the debtor bank initiates the payment to be sent to the creditor bank. MAV is commonly used for condominium and tuition fees, payments for school canteens and instalments for life insurance policies, etc. Collection request is usually sent in advance before the due date.

## Characteristics of the MAV

The MAV is a bulletin with a predetermined amount, which:

- Creditor's bank prints in the standard format
- Debtor receives by post
- Payable at any Italian bank or post office

This has all the payment data and is identified by a unique numeric code. The paper notice has the following information that creditor bank and creditor uses for reconciliation:

- Debtor’s name and surname
- Payment amount
- Reason for the transaction
- Payment expiration date (not mandatory for the payment transaction)
- Unique MAV number

## Initiation of MAV Payments

The `PAYMENT.ORDER (PO)` application is used to initiate and process MAV payments as a CT payment. It generates the message to clearing in a 403 Credit Transfer (CT) message format (flat file), which has multiple CT payments bulked in one file.

The single transactions processed in the interbank context are identified using the Codice Riferimento Messaggio (CRO). It is a unique reference number generated by combining the year (only YY of YYYY) with the Julian Date and 4 digit incremental number, divided by 13 and added with the 2 digit remainder at the end of the combined value. The CRO number is generated and mapped to the outgoing 403 message. The system raises the following accounting entries on the execution date T+0:

**Individual entry**

- Debit – Customer account (Value Date T+1)
- Credit – Suspense MAV (Value Date T+1)

**Settlement Entry (Bulk Entry)**

- Debit – Suspense MAV (Value Date T+1)
- Credit – Suspense settlement MAV account (Value Date T+1)

The Nostro account in `PP.CLEARING.SETTING` needs to be configured.

This warehouses the payment received after cut-off time for next day processing. It generates the outward 403 message with the following naming convention: BH.36003.ABHMS.[trailer]

where,

- [trailer] = yyyymmddhhmms
- 36003 is sender bank code

## Inward Return Message from Clearing

The Originator bank that initiates the 403 message can receive a return payment in the 405 message format. The primary 403 message is retrieved based on the MAV ID available in the 405 message. If the 403 message cannot be retrieved, it parks the payment in the Repair queue for manual action. On T+1 (value date), it posts the following entries in the customer account based on the return message:

- Debit - Suspense MAV
- Credit - Customer

The settlement entry with Nostro is not booked as part of the incoming 405 return message. The clearing sends a separate reconciliation 340 message based on which Temenos Payment Hub (TPH) posts settlement entries and reconciles with the Nostro account.

TPH does not support reconciliation messages. Posting based on reconciliation message is handled as local customisation.

## Support the Incoming Reconciliation Message

TPH processes the 340 message received from the clearing, maps the message information and displays the details in an enquiry format.

In this topic

- [Introduction to Mediante Avviso (MAV) Payment](#IntroductiontoMedianteAvvisoMAVPayment)

- [Characteristics of the MAV](#CharacteristicsoftheMAV)
- [Initiation of MAV Payments](#InitiationofMAVPayments)
- [Inward Return Message from Clearing](#InwardReturnMessagefromClearing)
- [Support the Incoming Reconciliation Message](#SupporttheIncomingReconciliationMessage)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:20:18 PM IST