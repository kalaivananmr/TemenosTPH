# Introduction to Interac Instant Payment via Central1 - Interacetransfer

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Canada/Canada/PPCAIC/Introduction.htm#InteraceTransfer

---

# Introduction to Interac Instant Payment via Central1

Updated On 06 October 2022 |
 6 Min(s) read

Feedback
Summarize

Interac e-Transfer is a fast secure and convenient way to send money to anyone in Canada using online banking. The participating bank or credit union transfers the funds using established and secure banking procedures. Transfers are almost instant but can take up to 30 minutes depending on your bank or credit union.

## Account Number Validation

ISO20022 instant messages can be consumed and processed using Instant Payments and Clearing Frameworks functionality available in Temenos Payments Hub (TPH).

This functionality is used to derive the Temenos Transact account number from the payment message received from Interac. As Interac sends the account number in different format, the same will be converted into the Temenos Transact account for posting into Temenos Transact.

The PPCAIC.INTERAC.ENRICH.API.ACCOUNT routine is used to derive the Temenos Transact account number based on the format received from the Interac messages.

The routine was attached as a hook routine in the *Enrich API* field from the PP.MSGMAPPINGPARAMETER application.

## Interac eTransfer

Central1 is implementing ISO20022 standards for all Interac instant messages. So, Temenos Transact should also support Interac Instant in ISO20022 standard.

The Interac adaptor is an interface that connects the Temenos Transact to a network (Central 1).

The list of ISO20022 messages received by banking host is provided below:

- PACS.008 (Initiate deposit (credit) of funds to account).
- PACS.002 (Confirm previous deposit (credit) instruction).
- PACS.003 (Initiate withdrawal (debit) of funds from account).
- PACS.002 (Confirm previous withdrawal (debit) instruction).
- PACS.007 (Reverse (undo) previous withdrawal debit or credit instruction).
- PACS.004 (Return previously withdrawn funds).
- Heart beat request (to check the bank host system is up and not offline).

The ISO20022 instant messages can be consumed and processed using the Instant Payments and Clearing Frameworks functionality available in Temenos Payments Hub.

This functionality allows banks to:

- Process the ISO20022 PACS.008 credit proposal message received from Central1.
- Process the ISO20022 PACS.002 credit confirmation message received from Central1.
- Process the ISO20022 PACS.003 debit proposal message received from Central1.
- Process the ISO20022 PACS.002 debit proposal confirmation message received from Central1.
- Process the ISO20022 PACS.007 reversal message received from Central1.
- Process the ISO20022 PACS.004 reversal message received from Central1.
- Process the heart beat request to check the bank host system is up and not offline.

The diagram below describes the flow of ISO20022 message from Interac to the banking host via central1.



[Design Time](#)

The design time process is explained below.

[Processing Credit Proposal and Confirmation Requests](#)

The customer receives an e-transfer or request money from Interac and will initiate the deposit request.

C1 sends the PACS.008 message to the banking host to validate the account for the credit process.

The banking host will receive PACS.008 and validate the account existence and respond back via PACS.002 for credit confirmation.

C1 sends the PACS.002 confirmation message to the banking host for to credit customer account.

The banking host will raise accounting entries to credit the customer account upon receiving the PACS.002 message.

The flow of initiating the deposit (credit) of funds to the account is provided below.



[Processing Debit Proposal and Confirmation Requests](#)

The customer sending the Interac instant request money will initiate debit request.

C1 initiates the debit proposal by sending the PACS.003 message to banking host.

The banking host will receive the incoming PACS.003 and validate the account. The response with the fee will be sent in PACS.002.

C1 sends the PACS.002 confirmation message to the banking host to debit the funds from the customer account.

The banking host confirms the debit to central1 by sending the PACS.002 message.

The flow of initiating the debit of funds to the account is provided below:



[Processing Reversal Requests](#)

If any of the above PACS.008 response fails to reach Interac then C1 will send a reversal message (PACS.007).

The banking host receives the PACS.007 message and credit’s the funds back to customer’s account (debited by previously made transaction).

The flow of processing reversal requests is provided below:



[Processing Return Requests](#)

When the customer cancels the sent transfer or recipients declining e-transfer, the return will be initiated to credit the customer’s account.

C1 initiate the credit funds to the customer account by sending the PACS.004 message to the banking host.

The banking host will receive the incoming PACS.004 and confirm the account existence with PACS.002.

C1 sends the PACS.002 confirmation message to the banking host to credit the customer’s account.

The banking host confirms the credit to central1 via PACS.002.

The flow of processing return requests is provided below:



[Run Time](#)

The overall flow of the request response message from Central1 to Temenos Transact through the Interac adapter layer and Temenos Payments Hub layer is provided below.



## Interac Instant Payment Clearing

This functionality allows banks, using the Interac instant payments in ISO8583 format, to accept, process and respond to the ISO20022 messages sent from Interac via the Canada Clearing Email Money Transfer (C1 EMT).

Temenos Payments Hub and the Temenos Transact (core system) will receive and process Interac instant payments.

The following are the Interac instant payment features for retail and commercial customers:

- Higher transactions limits (up to $25,000).
- Real-time confirmation messages.