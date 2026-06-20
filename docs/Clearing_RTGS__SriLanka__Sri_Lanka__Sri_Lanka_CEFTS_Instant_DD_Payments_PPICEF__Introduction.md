# Introduction to CEFTS Instant DD Payments

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/SriLanka/Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Sri Lanka > [Sri Lanka CEFTS Instant DD Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Introduction.htm) > Introduction

- Sri Lanka;)
  - [Sri Lanka Clearing Sri Lanka Clearing](../../Sri_Lanka/Sri_Lanka_PPLKRT/Introduction.htm)
  - [Sri Lanka Cheques Sri Lanka Cheques](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Introduction.htm)
  - [Sri Lanka Interbank Payment System Sri Lanka Interbank Payment System](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Introduction.htm)
  - [Sri Lanka CEFTS Instant CT Payments Sri Lanka CEFTS Instant CT Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Introduction.htm)
  - [Sri Lanka CEFTS Instant DD Payments Sri Lanka CEFTS Instant DD Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Introduction.htm)
    - [Introduction](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Introduction.htm)
    - [Configuration](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Configuring.htm)
    - [Working with](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Working_with.htm)
    - [Tasks](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Tasks.htm)
    - [Outputs](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Outputs.htm)

Payments

# Introduction to CEFTS Instant DD Payments

Updated On 08 November 2022 |
 7 Min(s) read

Feedback
Summarize

Lanka Pay Common Electronic Fund Transfer Switch (CEFTS) real-time payments is a 24x7 instant payment processing system, which processes domestic payments within Sri Lanka. It currently processes:

- Instant credit or debit transfers in LKR currency
- Retail and corporate payments with a maximum transaction limit of LKR 5 million

It routes and receives the payment from the beneficiary bank using CEFTS switch. Credit is available to the beneficiary in real time. Lanka pay operates in ISO8583 format (a text based fixed length) that is used to process card or Electronic Funds Transfer (EFT) transactions.

Bank-to-Bank settlement is accomplished in the domestic Real Time Gross Settlement (RTGS) system with settlement cycle from 2 PM (today) to 2 PM (next day).

## CEFTS Participants

CEFTS Instant Direct Debit (DD) payment supports direct participants. The participant details are manually captured in `CA.CLEARING.DIRECTORY`.

## Types of CEFTS DD Processing

The following are the two types of processing used for CEFTS DD:

[Outward Processing](#)

The processing activities involved in the payment flow in sequence for CEFTS instant DD processing is shown below.



| Activity | Description |
| --- | --- |
| CEFTS DD | Captures a CEFTS debit collection request from Collection Initiation page or Channels. Any error encountered during validation of fields (mandatory) are displayed on submission.  To know more, refer to [Capturing CEFTS Single Customer DD Payment (Manually)](Working_with.htm#Capturing_CEFTS_Single_Customer_DD_Payment_(Manually)). |
| System performs the following business validations on a DD collection request. If any error occurs, it cancels the request. | |
| Account validation | Validates whether a valid credit account is available in Temenos Transact |
| Bank code validation | Validates the receiving institution identifier code |
| Transaction limit | Validates the CEFTS transaction limit against payment amount (that is, LKR 5 million) To know more, refer to [Reachability in CEFTS](Configuring.htm#Reachability_in_CEFTS). |
| Time stamping | Timestamps the payments (in TPH) before sending it out. The waiting time is 30 seconds before time out. |
| Filtering | If there is a positive hit, TPH cancels the payment. |
| Routing | Routes the payment to a CEFTS direct participant bank based on the routing configurations setup in TPH. |
| Charge calculation | Configures the CEFTS transaction fees (if any), according to the bank specific requirements. |
| Outward payment generation | Generates payment request that complies to CEFTS schema defined in ‘CEFTS member bank interface specification’. It parks the payment in ‘Awaiting Acknowledgement (PSR)’ status. |
| Posting | Posts the following after confirmation:  - Debit – Clearing (suspense) - Credit – Customer |

[Inward Processing](#)

This section describes the inward CEFT DD transaction received from CEFTS clearing to an account in Temenos Payments Hub.



| Activity | Description |
| --- | --- |
| CEFTS inward DD received from Lanka pay | Receives an inward Direct Debit (DD) payment from Lanka pay  - Processes and responds the CEFT request with a payment response in real time. |
| System performs the following business validations when a CEFT DD is received from Lanka Pay: | |
| Account validation | Validates the debit account (if available in TPH and there are no restrictions) |
| Bank code validation | Validates the receiving institution identifier code |
| Transaction limit | Validates the CEFTS transaction limit against the payment amount (that is, LKR 5 million) |
| Debit authority (DD only) | Checks for debit mandate. If available the system executes the inward DD request. Mandate check is not required for Just Pay DD. |
| Balance check | Performs balance check on debtor account for payment amount.  - If sufficient funds are available, it reserves the required funds for processing the DD request. - If the balance check fails, it cancels the payment. |
| Filtering | If there is a positive hit, TPH cancels the payment and sends a negative PSR |
| Routing | Routes the payment to a CEFTS direct participant bank based on the routing configurations setup in TPH |
| Charges | Handles the charges locally |
| Generate PSR | Payment Status Response (MT210) to be responded back to the beneficiary bank |
| Postings | Posts the following before confirmation:  - Debit – Customer - Credit – Suspense |

## CEFTS Payment Status Response

The processing activities involved in the payment status response is shown below.



| Activity | Description |
| --- | --- |
| MT 210 received from CEFTS Lanka Pay to TPH | Receives Payment Status Response (PSR) in response to a previously sent CT or DD payment request. PSR can indicate a negative or positive response. The originating bank receives the PSR, when payment request generated by:  - Lanka Pay – Cannot be processed due to validation failure, issues with beneficiary bank or timeout - Beneficiary bank –   - Cannot be processed due to validation failures or issues with beneficiary account   - Is successfully accepted by the bank |
| Match PSR with payment | Matches the PSR with an original CT or DD |
| Update payment status | Payment status is updated as follows:  - If the response code in PSR is ‘Approve’, it marks the status as ‘Completed’ - If not, it marks the status as ‘Cancelled’ and maps the relevant CEFTS response codes with the payment. |

## CEFTS Reversal Request and Reversal Response Advice

The sending bank or Lanka Pay immediately initiates reversals to ensure that a sent payment is cancelled completely due to timeout or communication error.

| Activity | Description |
| --- | --- |
| Sending bank | A reversal is initiated in the following cases:  - Non-receipt of a PSR (MT210) for an already sent DD due to timeout or communication failure - Communication failure between the customer and bank  The sending bank needs to send a reversal (MT420) message and follow up by sending a reversal repeat (MT421) until a response (MT430) is received from Lanka Pay. This helps to ensure the cancellation of the transaction. |
| Lanka pay | If there is a delayed PSR (MT210) response from the beneficiary bank, Lanka Pay performs the following until a Reversal Advice (MT430) is received from the originating bank:  - Initiates a reversal request (MT420) message - Sends a reversal repeat (MT421) message |
| Receiving bank | On receipt of a reversal request (MT420), the receiving bank reverses the original transaction and sends a reversal advice response (MT430). |



In this topic

- [Introduction to CEFTS Instant DD Payments](#IntroductiontoCEFTSInstantDDPayments)

- [CEFTS Participants](#CEFTSParticipants)
- [Types of CEFTS DD Processing](#TypesofCEFTSDDProcessing)
- [CEFTS Payment Status Response](#CEFTSPaymentStatusResponse)
- [CEFTS Reversal Request and Reversal Response Advice](#CEFTSReversalRequestandReversalResponseAdvice)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:44:30 PM IST