# Introduction to SGMEPS in ISO20022 (MX) - Introductiontosgmepsiniso20022Mx

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Singapore/Singapore/PPSGMX/Introduction.htm#IntroductiontoSGMEPSinISO20022MX

---

# Introduction to SGMEPS in ISO20022 (MX)

Updated On 12 April 2026 |
 6 Min(s) read

Feedback
Summarize

The MAS Electronic Payment System (MEPS) is a real-time gross settlement (RTGS) system developed for large-value Singapore dollar interbank funds transfers and the settlement. Each transaction is processed individually in real time and settled upon receipt via a highly secure electronic network. Settlement of funds is immediate, final and irrevocable. Singapore MEPS RTGS is a swift based clearing.

The Customer Credit Transfer message (pacs.008) is from payer participant bank to payee participant bank via copy message to MEPS RTGS for funds settlement.

The Customer Credit Transfer Straight through processing (STP) Transfer message is from payer participant bank to payee participant bank via copy message to MEPS RTGS for funds settlement.

The Financial Institution Credit Transfer message (pacs.009) is from payer participant bank to payee participant bank via copy message to MEPS RTGS for funds settlement.

The Financial Institution Credit Transfer message (pacs.009 COV) is from payer participant bank to payee participant bank via copy message to MEPS RTGS for funds settlement. This financial institution transfer provides cover for an underlying customer credit transfer.

TPH receives xsys.003 (Rejection Notification) from SWIFT to notify that the payment instruction has been refused by the clearing and the reason for the refusal.

The Payment Cancellation Request (camt.056) is from participants to cancel queued or future-dated pacs.008 /pacs.008 STP transactions and queued or future-dated pacs.009 / pacs.009 cov transactions.

The user can initiate cancellation request Camt.056 for SG MEPS payments using an enquiry, for which no notification message is received.

TPH can receive camt.029 from the clearing as a response to the sent camt.056 with the following statuses:

- CNCL when the cancellation is accepted
- RJCR when the cancellation is rejected

TPH receives xsys.002 (Authorization Notification) from SWIFT to notify that the payment instruction has been accepted by the clearing.

As part of Singapore MEPS credit transfer flow, the configurations are released for outgoing and incoming pacs.008, pacs.009, pacs.009 COV message.

- Mapping and Model Configuration has been developed to generate outgoing pacs.008, pacs.009 and pacs.009 COV via Payment Order Application (POA) and Order Entry Application (OE).
- Mapping and Model Configuration to receive Incoming pacs.008, pacs.009, pacs.009 COV and xsys.003, Camt.029 and Xsys.002.
- Mapping and Model Configuration to generate outgoing camt.056 message.

## SG MEPS+ 2026 Rulebook Changes

As part of the SG MEPS+ 2026 Rulebook Changes,

- The *Address Line* field supports Unstructured option for CBPR+ interoperability. As a result, the *Country* and *Town Name* fields are made optional in the following message types:
  - **pacs.008** and **pacs.008 STP** – For Previous Instructing Agent 2 and 3, Intermediary Agent 2 and 3, and Related Remittance Information.
  - **pacs.009** – For Previous Instructing Agent 2 and 3 and Intermediary Agent 2 and 3.
  - **pacs.009 COV** – For Previous Instructing Agent 2 and 3, Intermediary Agent 2 and 3, and Underlying Customer Credit Transfer (Previous Instructing Agent 2 and 3, and Intermediary Agent 2 and 3).

    The PrvsInstgAgt element is not applicable for Outgoing payments.
- The *Name* field supports a maximum of 140 characters in the following message types:
  - **pacs.008** and **pacs.008 STP** – For the Debtor, Debtor Agent, Creditor Agent, Creditor, and UltmtCdtrr elements.
  - **pacs.009** - For the Debtor, Debtor Agent, Creditor Agent, and Creditor elements.
  - **pacs.009 COV** – For the UndrlygCstmrCdtTrf/Cdtr, UndrlygCstmrCdtTrf/Dbtr, UndrlygCstmrCdtTrf/CdtrAgt, UndrlygCstmrCdtTrf/DbtrAgt, and UndrlygCstmrCdtTrf/UltmtCdtr elements.
- The *End to End Identification* field supports a maximum of 35 characters in the **pacs.009** and **pacs.009 COV** messages.
- Extended characters are supported for CBPR+ interoperability in the following message types:
  - **pacs.008** - For the Debtor, Debtor Agent, Instructing Agent, Instructed Agent, Creditor Agent, Creditor and Remittance Information elements.
  - **pacs.008 STP** – For the Debtor, Instructing Agent, Instructed Agent, Creditor, and Remittance Information elements.
  - **pacs.009** – For the Debtor, Instructing Agent, Instructed Agent, Creditor Agent, and Creditor elements.
  - **pacs.009 COV** – For the Debtor, Instructing Agent, Instructed Agent, Creditor Agent, and Creditor elements. In Underlying Customer Credit Transfer - for Debtor, Debtor Agent, Creditor Agent, Creditor and Remittance Information elements.
- The *BICFI in Charges Information* field is made optional in the **pacs.008** message.
- The *Postal Address Field* supports Hybrid Address for parties and agents in the **pacs.008**, **pacs.008 STP**, **pacs.009**, and **pacs.009 COV** messages. As part of Hybrid Address, *Town* and *Country* fields are mandatory and at least one line of *Address Line* is supported.
- Party elements support only Name (with or without address) in the following message types;
  - **pacs.008 and pacs.008 STP** – For Creditor, Debtor, Initiating Party, Ultimate Creditor,  and Ultimate Debtor elements.
  - **pacs.009 COV** – Under Underlying Customer Credit Transfer for the Creditor, Debtor, Initiating Party, Ultimate Creditor, and Ultimate Debtor elements.
- A fixed value is updated under BAH Business Service to mas.mep.02, mas.mep.stp.02, mas.mep.cov.02 for the **pacs.008/pacs.009**, **pacs.008 STP**, and **pacs.009COV** messages respectively. The same value is updated in Request Subtype of the Swift InterAct network header.