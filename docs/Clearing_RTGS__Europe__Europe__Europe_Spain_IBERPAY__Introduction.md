# Introduction to Spain IBERPAY Instant Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_Spain_IBERPAY/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm) > Introduction

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
  - [Euro Swiss Interbank Clearing Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
    - [Introduction](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
    - [Configuration](../../Europe/Europe_Spain_IBERPAY/Configuration.htm)
    - [Working With](../../Europe/Europe_Spain_IBERPAY/WorkingWith.htm)
    - [Tasks](../../Europe/Europe_Spain_IBERPAY/Tasks.htm)
    - [Outputs](../../Europe/Europe_Spain_IBERPAY/Outputs.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Introduction to Spain IBERPAY Instant Clearing

Updated On 03 December 2024 |
 4 Min(s) read

Feedback
Summarize

Iberpay Instant is a payment system designed to process SEPA Credit Transfers (SCT) instantly. It enables immediate payment transfers between entities, operating 24x7x365 a year. With Iberpay Instant, each credit transfer is completed within a round-trip time of 20 seconds, ensuring that the payment is processed and settled without delay.

As a Direct Participant of IBERPAY Instant clearing (IPAYINST), TPH is capable of receiving and processing inward customer transfer payments through IBERPAY.

When a payment is received from Clearing, the system checks if it is within the overall timeout, before accepting the message and processing it.
Before sending a confirmation to the Clearing, the system does not check if the payment is within the overall timeout. If the payment exceeds the overall time, the Clearing rejects the payment.

The Originator Bank participant (in the Iberpay Instant Payment Clearing) can request a recall of a previously settled Instant Payment transaction within the prescribed number of days following the Interbank settlement date. Iberpay Instant payment clearing then forwards the payment cancellation request to the Beneficiary Bank participant.
For recalls of its own payments, if the Beneficiary agrees to return the payment, the return payment is generated and sent to the Clearing. The status of the payment cancellation request is updates as **Closed**, after updating the return payment details against it. The system must support the generation of ISO20022 pacs.004 payment return message.
If the beneficiary does not provide consent to return the payment, a negative answer is generated to the Originator bank through the clearing, as a Resolution of Investigation (ROI) message (camt.029).

Iberpay Payment Clearing can inquire on the status of an instant payment order forwarded to the Beneficiary Bank. When a request for status update (pacs.028) is received by the beneficiary bank and the bank has already processed the recall request, then the following steps must be performed based on the response of the recall request:

- If the recall request was already accepted (i.e. a return payment was sent to the originator bank), then a camt.029 (negative response) with status ‘ARDT’ must be generated as a response to the request for status update.
- If the recall request was already rejected (i.e. a camt.029 was sent to the originator bank), then a camt.029 (negative response) with the original reject reason code must be generated again as a response to the request for status update.

This document covers the inward flow, which includes Incoming pacs.008, outgoing pacs.002, Incoming pacs.002, incoming pacs.028, incoming camt.056, outgoing camt.029 and outgoing pacs.004.

The Existing ESIBER feature of TRS is replaced with the new Clearing product **PPESII**, and new configurations have been released under PPESII. Any new regulatory or rulebook changes will be accommodated into this new PPESII module.

In this topic

- [Introduction to Spain IBERPAY Instant Clearing](#IntroductiontoSpainIBERPAYInstantClearing)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:22:03 PM IST