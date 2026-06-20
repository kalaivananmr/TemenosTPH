# Introduction to Hong Kong Faster Payments System (HK FPS) - Paymentstatusenquiry

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/HongKong/Hong_Kong_PPHINS/Misc/Introduction.htm#PaymentStatusEnquiry

---

# Introduction to Hong Kong Faster Payments System (HK FPS)

Updated On 18 February 2026 |
 18 Min(s) read

Feedback
Summarize

Hong Kong Faster Payment System (HK FPS or FPS) is a 24x7 instant payment processing system that processes domestic payments within Hong Kong. It can perform the following:

- Process both credit transfers and direct debits
- Operate in HKD and CNY currencies
- Process retail and corporate payments

Since there are no specific limit set for the payments, the bank can decide on their risk limit. HK FPS has a payment switch to perform the following:

- Validate the payments
- Update risk and settlement accounts of the participants
- Route the payment to destination bank

The beneficiary bank provides credit to the beneficiary in real time or near-real time with SLAs that varies from few seconds to hours. This depends on the level of participation of the receiving bank in HK FPS scheme. HK FPS also allows initiation of payments through alternate identifiers (proxy), such as mobile number. The alternate account needs to be linked to a credit account number of the sending bank before initiating the payment. This is done against a central directory hosted by HKICL (known as addressing service). This feature operates in iso20022 format (xml-based), and performs Bank-to-Bank settlement in real-time basis (gross) in the respective currencies.

## System Context



|  |  |
| --- | --- |
| Temenos Payment Hub (TPH) | Allows the user to capture HK FPS instant payments along with inward and outward payments processing. |
| ESB | Enables interface gateway of Temenos payment system to interact with HK FPS clearing. The payment system interacts with the following:  - ESB through internal Temenos format - ESB interface (with HK FPS clearing) through iso20022 format |
| HK FPS | Hong Kong Faster Payment Services |
| Bank Host Systems | Bank systems (that is, Temenos Payments Hub system interface) to process supplement payments. Additionally, it can have Straight-Through Processing (STP) channels to send payment initiation files (pain.001), which can come directly to payment system. Therefore, the payment system can process the files (received) and send it to clearing. |

## Types of HK FPS Participants

Banks can participate in HK FPS as one of the following participants:

| Participant | Description |
| --- | --- |
| Settlement | A member bank that sends payment directly to HK FPS, and holds a settlement account with the central bank (HKDSI or CNYCB). |
| Clearing | A non-bank participant of HK FPS (wallet companies known as Stored Value Cards) that sends payment directly to HK FPS but settles through an account of a settlement participant. The settlement participant needs to authorised all transactions sent by clearing participant, before it is cleared by HK FPS. |

## Types of Payment

FPS offers the following business services that a bank can subscribe based on their payment business demands:

- Type C1 – A single instant credit transfer payment that is processed in real time
- Type C2 – A single credit transfer payment in near-real time
- Type C3 – A bulk credit transfer (out of scope)

Once subscribed, the bank needs to adhere to the business rules and operating procedures.

The sending bank can recommend the type of business service for payments in the *Business Service* field. A bank can initiate a payment with a business service that is subscribed it. FPS validated whether the receiving bank can receive a payment with a particular business service before processing the request forward.

## HK FPS Credit Transfer Processing Modes

The sending bank can recommend the Credit Transfer (CT) processing mode in the payment message (in the *Local Instrument Proprietary* field as AV or WAV). HK FPS performs the following on receipt of payment request from a sending bank:

| Credit Transfer with Account Verification (AV) | |
| --- | --- |
| Requests the beneficiary bank to verify the beneficiary account (if it is available and suitable for credit) before settling the payment within FPS.  - If the beneficiary bank responds positively, it performs the settlement. - If the beneficiary bank responds negatively, it rejects the payment request. | On receipt of an AV payment from a sending bank, where FPS finds that the beneficiary bank:  - Can process the AV payment, it raises an AV entry to the beneficiary bank. - Cannot process the payment, then the business services payment:   - C1 – Rejected   - C2 – Converted to without Account Verification (WAV) |
| Credit Transfer without Account Verification (WAV) | |
| HK FPS settles the payment and forwards it to the beneficiary bank. If the beneficiary bank cannot credit the payment, it can initiate a return payment separately (within defined recourse period) as a post settlement return. | On receipt of a WAV payment from a sending bank, where the FPS finds that beneficiary bank:  - Can process the WAV payment, it checks the processing mode of the beneficiary bank,  - C1 – Processed or rejected   - C2 – Processed irrespective of the mode of the beneficiary bank  - Cannot process the payment, then it is rejected (irrespective of business service). |

## Types of Messages

HK FPS supports the following message types:

| Message | Description |
| --- | --- |
| pacs.008 | Payment Request  - Submitting bank sends it to HK FPS - Receiving bank receives it from HK FPS |
| pacs.002 | Payment Response, also known as Payment Status Report (PSR)  - Sending bank receives it from HK FPS in response to pacs.008 - Receiving bank sends it in response to Account Validation (AV) request - Sending bank receives it in response to a payment status request (pacs.028) sent earlier to HK FPS |
| pacs.004 | Payment Return  - Beneficiary bank sends it to HK FPS to return an inward payment - Sending bank receives it from HK FPS as a return for an outgoing payment sent earlier |
| pacs.028 | Payment Status Request  - HK FPS receives it that inquire on the status of payment, which was sent earlier to FPS (but have not got a response or for a completed payment after a period of 7 days) |
| camt.056 | Payment Cancellation Request  - HK FPS sends it as a cancellation request to beneficiary bank during timeout and settlement failure |

## Manual Capture of HK FPS Payments

Temenos payment solution offers payment capture screen for the following HK FPS payment types:

- Credit Transfer with Account Verification (Type C1 and C2)
- Credit Transfer without Account Verification (Type C1 and C2)

## Clearing Cut-Off

FPS is configured in the system as a clearing that supports 24x7 operations, hence, cut-off validations are not effective (even when configured).

## Reachability

In all outward HK FPS payments, reachability of the beneficiary bank (through HK FPS) is validated against HK FPS directory. It is performed by using the National Clearing Code (NCC) of the beneficiary bank.

The beneficiary bank reachable only when the NCC is available in the clearing directory.

## Participant Bank SLA (Beneficiary Bank) for AV Payments

The maximum time allowed for a beneficiary bank to respond to an Account Verification (AV) request is as follows:

- Type C1 or C2 Payment – 5 seconds

## Returns

The following are the types of returns:

| Type of return | Description |
| --- | --- |
| Pre-Credit | Payee bank is unable to credit funds to the beneficiary for a received inward payment. The operation user automatically or manually returns the payments.  - Automatic return is sent after the payment is received - Manual returns is sent within 7 days of payment receipt   This is applicable only for WAV mode. |
| Post Credit | Beneficiary bank can initiates the returns on request of a payee, within 7 days of payment receipt. It can also debit the original payee as part of the returns processing. This is applicable for AV and WAV. |

## Cancellations

HK FPS sends cancellations to the payee’s bank during timeout or failure in settlement. These cancellations (camt.056) are applicable only for synchronous mode (payments which require account verification) of processing, where HK FPS requires a response to a payment request within a predefined time period or balance is insufficient in settlement accounts. On receipt of cancellation request, the payee’s bank cancels the original payment and FPS does not require a response for a camt.056 that is sent. If the original payment is not found, the cancellation is routed to repair for manual action.

## Payment Status Enquiry

The payer’s bank manually initiates the payment status enquiry (pacs.0028) and sends it to HK FPS to find the status of an outward payment. This is performed when the debtor wants to know the status of the payment. All the payment messages are stored in FPS for a period of 7 days after which the information is removed. CI rejects the enquiry request from payer’s bank that is older than 7 days from the payment receipt date.

## Outward Processing – Payment Request

The outward payment processing involves `PAYMENT.ORDER (PO)` application and TPH modules. The below workflow shows the processing activities involved in the payment.



| Activity | Description |
| --- | --- |
| Manual capture of CT | Captures a HK FPS credit transfer from `PO` application page. Validates mandatory and non-mandatory fields on submission and displays an error (if any). To know more, refer to [Manual Capture of Credit Transfer with or without account verification.](Working_with.htm#_Manually_capturing_a) `PO` application page cannot be used to perform proxy based manual capture. |
| System performs the following business validations on payments: If the validation fails, it parks the payments in Repair queue for user action. | |
| Account validation | - Validates whether a valid debit account is available in Temenos Transact - Fetches Debtor IBAN from Temenos Transact database (if not available in instruction) |
| Bank code validation | Does not validate the bank codes that the user has entered |
| Duplicate check | Does not perform duplicate checks during initiation, as it is not mandated by Scheme Rules Bank can configure this feature according to their requirements. |
| Transaction limit | Validates the HK FPS transaction limit against payment amount. To know more, refer to [Limits](../../../../../T24_Transact/Derivatives_Structured_Products/DX/Derivatives/Limits/Introduction.htm). |
| Reachability check | Validates whether the beneficiary bank (clearing code) is reachable directly or indirectly. To know more, refer to [Reachability](Configuration.htm#_Reachability_in_HKFPSINST). |
| Payment Simulation is applicable when a payment is manually captured (using `PO` application page or customer facing channels interacting with the application). During simulation, the system performs the following:  - Calculates the applicable charges, value date and exchange rate (if Foreign Exchange is involved) - Displays it to the user to receive a confirm to submit or abandon the payment  Simulation is performed by TPH (if installed) or `PO` application when the payment system is external. | |
| Account restrictions | Validates posting restrictions on the following:  - Debit account - Credit account (if it is an own account, that is, within the same bank).  If the account has restrictions, it cancels (if manually captured) the payment or sends negative PSR. |
| Cut-off check | HK FPS is a 24x7 system that operates with no clearing cut-off. Hence, the payment is not validated. |
| Dates calculation | Acceptance date time, execution, credit value and debit dates are similar to the current system date. |
| Charge calculation | Calculates all the applicable charges for the payment (if configured) |
| Balance check | Performs balance check on debtor account for total value of payment amount and charges. If sufficient balance is not available in the account, it cancels the payment order. |
| The user needs to perform the following actions:  - On submission of the payment after simulation, it waits for supervisor approval.  - Once approved, the payment is moved for further processing. - If rejected, it is modified and resubmitted for approval. | |
| Fraud check | - Sends a fraud check request to the Fraud Check Engine - Updates the status of the payment on receiving the response.   Payment can be set to Cancelled or Continue processing based on the configuration.  To know more, refer to [Fraud Check](../../Payment_Initiation_(PI)/Fraud_Check/Introduction.htm#top) in Payment Initiation. |
| Send payment to payment system | Sends the payment order to the payment system for execution.  - If the payment system is TPH, it embeds the transfer between `PO` application and TPH. - If the payment system is third party (not Temenos), `PO` application generates the payment initiation message (pain.001).   Payment system acknowledges the receipt of the Payment Initiation (PI) message in both cases and changes the payment status to ‘Placed’. |
| Time stamping the payment | HK FPS payment cannot carry timestamp. It calculates the SLA and not the participant banks. |
| Filtering | Performs filtering of payments (if configured). This is a bank specific requirement and is handled during implementation. |
| Routing | Routes the payment to a clearing channel (HK FPS), which moves it to HK FPS (through IIB). The clearing channel is involved in determining the message type (HK FPS pacs.008). |
| Charge calculation | Calculates the charges applicable for the payment that is processed. This is displayed as debit side charges in the payment after this activity. This charge is similar to the value calculated during simulation, unless it is changed due to simulation activity.  During implementation, all fees (includes HK FPS transaction fees) are set according to specific requirements of the bank. |
| Funds reservation | Reserves the funds on the debit account. This is performed during implementation, according to the specific requirement of the bank.  To reserve funds, perform the configuration in the following fields in the `PP.BALANCE.CHECK.REQUIRED` table:   - *Source* - *Account Type* - *Message Type*   TPH performs funds reservation as follows:   - If Account Management System (AMS) is Temenos Transact, it is done in embedded mode. - If the AMS is external, it generates the request in a standard XML format and accepts response from the external system. |
| Debit posting | Debits the payment amount and charges to be borne by the customer to the Debtor’s account.  - If posting fails due to insufficient funds, it cancels the payment.  TPH performs debit posting as follows:  - If Account Management System (AMS) is Temenos Transact, it is done in embedded mode. - If the AMS is external, it generates the request in a standard XML format and accepts response from the external system. |
| Outward payment generation | Generates the payment request (by IIB) that complies to HK FPS schema defined in pacs.008.001.06. It parks the payment ‘Awaiting PSR’ status. |

## Inward Processing – Payment Request (pacs.008)



| Activity | Description |
| --- | --- |
| HK FPS payment received from CI | Receives an inward payment as follows:  - CT request with account verification – It processes and responds (with a payment response) in real time - CT request without account verification – It processes in near-real time or same day   TPH process both the payment types using the same workflow. |
| System performs the following business validations when a pacs.008 is received from HK FPS: | |
| Duplicate check | Validates whether HK FPS ID is duplicated within the last 7 business days (if configured). It does not check the Message ID or TXID of pacs.008. The Message ID is not similar to the value that the originating bank sends to HK FPS. |
| Resolution of proxy ID | Fetches the account (BBAN) corresponding to the Customer ID (which has a associated primary account). Hence, specific bank logic is performed in the site. Proxy ID is only for information in the inward message and not used by TPH. |
| Account validation | Validates and derives the beneficiary account from Customer ID (if proxy IDs are used):  - Beneficiary account closed - Beneficiary account stopped - Beneficiary account name does not match Beneficiary account number - Account is not in currency quoted |
| Bank code validation | Not Applicable |
| Account restrictions | Validates the restrictions on beneficiary account  - Debit or credit freeze or both |
| If any of the above validations fails, it sends the request (pacs.004) back to clearing. | |
| Calculate charges | Beneficiary bank can collect the charges, when the charge code is ‘SLEV’. |
| Beneficiary credit posting | Books the beneficiary with payment amount minus the applicable charges (with the value date in *Interbank Settlement Date*). This applicable only for WAV flow. |
| Generate account verification result | Generates an account verification result in HK FPS (pacs.002 format) for a payment |
| Settlement confirmation and posting | On receipt of settlement confirmation message from HK FPS, TPH performs the accounting. This applicable only for AV flow. |

Generation of payment status report is based on the need for account verification.

## FATF check for HKFPS payments

Hongkong Faster Payment System, HK-FPS or FPS is a 24x7 instant payment and Batch payment processing system that processes domestic and Cross border payments. Batch is non-instant clearing scheme in FPS, these payments are treated as non RTGS, non-instant payments.

As per regulations, to determine FATF check Debtor & Creditor related tags (Account No/IBAN, Name, Address, Country) are mandatory. For HKFPS domestic transfers address, country tags are not available as per message specifications. Hence, FATF check must be skipped for domestic transfers only.

An enhancement to an existing validation created for HKFPS payments to determine FATF check.

.