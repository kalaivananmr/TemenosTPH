# Introduction to CEFTS Instant CT Payments

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/SriLanka/Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Sri Lanka > [Sri Lanka CEFTS Instant CT Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Introduction.htm) > Introduction

- Sri Lanka;)
  - [Sri Lanka Clearing Sri Lanka Clearing](../../Sri_Lanka/Sri_Lanka_PPLKRT/Introduction.htm)
  - [Sri Lanka Cheques Sri Lanka Cheques](../../Sri_Lanka/Sri_Lanka_Cheques_PPLCIT/Introduction.htm)
  - [Sri Lanka Interbank Payment System Sri Lanka Interbank Payment System](../../Sri_Lanka/Sri_Lanka_Interbank_Payment_System_PPLNCL/Introduction.htm)
  - [Sri Lanka CEFTS Instant CT Payments Sri Lanka CEFTS Instant CT Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Introduction.htm)
    - [Introduction](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Introduction.htm)
    - [Configuration](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Configuring.htm)
    - [Working with](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Working_with.htm)
    - [Tasks](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Tasks.htm)
    - [Outputs](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_CT_Payments_PPICEF/Outputs.htm)
  - [Sri Lanka CEFTS Instant DD Payments Sri Lanka CEFTS Instant DD Payments](../../Sri_Lanka/Sri_Lanka_CEFTS_Instant_DD_Payments_PPICEF/Introduction.htm)

Payments

# Introduction to CEFTS Instant CT Payments

Updated On 08 November 2022 |
 8 Min(s) read

Feedback
Summarize

Lanka Pay Common Electronic Fund Transfer Switch (CEFTS) real-time payments is a 24x7 instant payment processing system, which processes domestic payments within Sri Lanka. It currently processes:

- Instant credit or debit transfers in LKR currency
- Retail and corporate payments with a maximum transaction limit of LKR 5 million

It routes and receives the payment from the beneficiary bank using CEFTS switch. Credit is available to the beneficiary in real time. Lanka pay operates in ISO8583 format (a text based fixed length), that is used for card or Electronic funds transfer (EFT) transactions processing.

Bank-to-Bank settlement is accomplished in the domestic Real Time Gross Settlement (RTGS) system with settlement cycle from 2 PM (today) to 2 PM (next day).

## CEFTS Participants

CEFTS Instant Credit Transfer (CT) payment supports direct participants. The participant details are manually captured in `CA.CLEARING.DIRECTORY`.

## Types of CEFTS CT Processing

The following are the two types of processing used for CEFTS CT:

[Outward Processing](#)

Outward CEFTS CT processing involves Payment Order (`PO`) application and Temenos Payments Hub. The processing activities involved in the payment flow in sequence is shown below.



| Activity | Description |
| --- | --- |
| CEFTS CT | Captures a CEFTS instant payment from PO application or Channels.  Any error encountered during validation of fields (mandatory and non-mandatory) are displayed on submission. To know more, refer to [Capturing the CEFTS Single Customer Payment (Manually)](Working_with.htm#Capturing_the_CEFTS_Single_Customer_Payment_(Manually)). |
| System performs the following business validations on payments: If the validation fails, it rejects the payment for user action. | |
| Account validations | Validates whether a valid debit account is available in Temenos Transact |
| Bank code validations | Validates the receiving institution identifier code |
| Transaction limit | Validates the CEFTS transaction limit against the payment amount (that is, LKR 5 million) To know more, refer to [Payment Order Product](Configuring.htm#Payment_Order_Product). |
| Reachability check | Validates whether the beneficiary bank is reachable through CEFTS payment scheme To know more, refer to [Reachability in CEFTS](Configuring.htm#Reachability_in_CEFTS). |
| Payment Simulation is applicable when a payment is manually captured (using PO application or customer facing channels interacting with the application). During simulation, the system performs the following:  - Calculates the applicable charges, value date and exchange rate (if Foreign Exchange is involved) - Displays it to the user to receive a confirm to submit or abandon the payment  Simulation is performed by TPH (if installed), or PO application when payment system is external. | |
| Account restrictions | Validates posting restrictions on debit account |
| Dates calculation | Execution, credit value and debit date are similar to the current system date |
| Charge | Calculates the applicable charges for the payment (if configured) |
| Balance check | Performs balance check on debtor account for payment amount.  If sufficient balance is not available in the account, it follows the excess authorisation workflow. |
| Fraud | Performs bank-specific integration |
| Send payment to system | Sends the payment order to the payment system for execution.  If the payment system is Temenos Payment Hub (TPH), it embeds the transfer between PO application and TPH. Payment system acknowledges the receipt of the Payment Initiation (PI) message and sends the payment to ‘PLACED’ status in PO application. |
| Time stamping the payment | Timestamps the payment (in TPH) before sending it out. - The waiting time is 30 seconds before time out. - Lanka Pay waits for 15 sec before timing out a transaction. |
| Filtering | If there is a positive hit, TPH cancels the payment. |
| Routing | Routes the payment to a CEFTS direct participant bank, based on the routing configurations setup in TPH |
| Charge calculation | Configures the CEFTS transaction fees (if any) according to the bank specific requirements |
| Funds reservation | Reserves funds on the debit account |
| Outward payment generation | Generates payment message that complies to CEFTS schema defined in ‘CEFTS member bank interface specification’. It parks the payment in ‘Awaiting Acknowledgement’ (PSR) status. |
| Posting | Posts the following before confirmation:  - Debit Customer - Credit CEFTS payable (suspense) |
| Manual queue repair | If the CEFT transaction initiated through PO application fails (due to any exception), system cancels the payment. |

[Inward Processing](#)

This section describes the inward CEFT CT transaction received from CEFTS clearing to an account in Temenos Payments Hub.



| Activity | Description |
| --- | --- |
| CEFTS CT payment received from Lanka Pay | Receives an inward Credit Transfer (CT) payment from Lanka Pay  - Processes and responds the CEFT request with a payment response in real time  To know more, refer to [Viewing CEFTS Received Files or Messages – Enquiry](Working_with.htm#Viewing_CEFTS_Received_Files_or_Messages). |
| System performs the following business validations when an MT200 (ISO8583) is received from Lanka Pay: | |
| Account validation | Validates the beneficiary account for the following:  - Beneficiary account number unknown - Beneficiary account closed |
| Bank code validation | Validates against Sri Lanka bank directory |
| Account restrictions | Validates restriction on beneficiary account Account does not permit credits. |
| Beneficiary credit posting | Books the beneficiary with payment amount after receiving the inward CT |
| Generate PSR | Generates a payment status report (MT210) with response code according to the Lanka pay specification |
| Filtering | If there is a positive hit, TPH cancels the payment and sends a negative PSR |
| Postings | Posts the following before confirmation:  - Debit Clearing Suspense - Credit Customer |

## CEFTS Payment Status Response

The processing activities involved in the payment status response is shown below.



| Activity | Description |
| --- | --- |
| MT 210 received from CEFTS Lanka Pay to TPH | Receives Payment Status Response (PSR) in response to a previously sent CT or DD payment request. PSR can indicate a negative or positive response. The originating bank receives the PSR, when payment request generated by:  - Lanka Pay – cannot be processed due to validation failure, issues with beneficiary bank or timeout - Beneficiary bank –   - Cannot be processed due to validation failures or issues with beneficiary account   - Is successfully accepted by the bank |
| Match PSR with payment | Matches the PSR with an original CT or DD |
| Update payment status | The payment status is updated as follows:  - If the response code in PSR is ‘approve’, it marks the status as ‘Completed’ - If not, it marks the status as ‘Cancelled’ and maps the relevant CEFTS response codes with the payment. |

## CEFTS Reversal Request and Response Advice

The sending bank or Lanka pay immediately initiates reversal to ensure that a sent payment is cancelled completely due to timeout or communication error.

|  |  |
| --- | --- |
| Sending bank | A reversal is initiated in the following cases:  - Non-receipt of a PSR (MT210) for an already sent CT due to timeout or communication failure - Communication failure between the customer and bank  The sending bank needs to send a reversal (MT420) message and follow up by sending a reversal repeat (MT421) until a response (MT430) is received from Lanka Pay. This helps to ensure the cancellation of the transaction. |
| Lanka pay | If there is a delayed PSR (MT210) response from the beneficiary bank, the Lanka pay performs the following until a Reversal Advice (MT430) is received from the originating bank:  - Initiates a reversal request (MT420) message - Sends a reversal repeat (MT421) message |
| Receiving bank | On receipt of a reversal request (MT420), the receiving bank reverses the original transaction and sends a reversal advice response (MT430). |



In this topic

- [Introduction to CEFTS Instant CT Payments](#IntroductiontoCEFTSInstantCTPayments)

- [CEFTS Participants](#CEFTSParticipants)
- [Types of CEFTS CT Processing](#TypesofCEFTSCTProcessing)
- [CEFTS Payment Status Response](#CEFTSPaymentStatusResponse)
- [CEFTS Reversal Request and Response Advice](#CEFTSReversalRequestandResponseAdvice)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:44:23 PM IST