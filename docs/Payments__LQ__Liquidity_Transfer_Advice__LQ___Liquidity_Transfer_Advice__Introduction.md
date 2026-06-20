# Introduction to Liquidity Transfer Advice

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/LQ/Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Liquidity Transfer Advice > Introduction

- Liquidity Transfer Advice;)
  - [Introduction](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Introduction.htm)
  - [Configuration](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Configuration.htm)
  - [Working with](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Working_wtih.htm)
  - [Tasks](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Tasks.htm)
  - [Outputs](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Outputs.htm)
- Liquidity Transfer Request;)

Payments

# Introduction to Liquidity Transfer Advice

Updated On 22 March 2025 |
 7 Min(s) read

Feedback
Summarize

Liquidity Transfer Advice (LTA) are advices that are received from an Account Holding Institution (AHI) to notify a balance or position update to the account held with the institution. The account holding institutions are typically a Clearing and Settlement Mechanism (CSM) such as, Real-Time Gross Settlement (RTGS) or a bilateral correspondent bank.

LTA may represent a credit advice or a debit advice depending upon the account being credited or debited respectively.

- The bank receives LTA from an RTGS system (in which the bank is a direct participant) when the bank’s RTGS settlement account balance is adjusted due to a liquidity adjustment transfer. A liquidity adjustment transfer are certain transfer operations performed by the central bank or by the bank's treasury operations in the RTGS settlement accounts.
- LTA arising from settlement process in RTGS where the bank is a participant to a Clearing.

## Co-Management

In certain RTGS’, the indirect participant banks can maintain liquidity management / cash accounts within RTGS, while delegating the management of such account to another bank, typically its agency bank (which is also a direct participant to the RTGS). This feature is called co-management. The bank that manages cash accounts for the indirect participant banks is called the co-manager, while the bank that has delegated the management of its cash account is called the co-managee.

The co-manager has the authority to action upon the co-managed entity’s cash account. Actions could include:

- Funding and de-funding the co-managee’s account.
- Executing overnight deposits and lending operations on the co-managee’s account.
- More actions related to account maintenance and limits (not in scope of LTA functionality)

RTGS sends LTAs to the co-manager bank when the balance of the co-managee cash account changes due to above mentioned operations.

TPH supports banks acting as co-manager by allowing to process LTA received from RTGS on liquidity adjustments occurring on the co-managee’s account.

## Processing LTA at Temenos Payments Hub

Temenos Payments Hub subscribes to only certain CAMT messages, such as LTA (camt.054 message) and from a certain sender address (such as, European Banking Authority (EBA), Banking Identification Code (BIC)). Temenos Payments Hub receives the LTA and processes them as book payments based on the configuration.

Temenos Payments Hub stores and qualifies the LTA as a payment, resolves the accounts, and performs posting of the LTA payment. The user can also repair LTA payments that failed processing.

Temenos Payments Hub also subscribes LTAs that failed format validation or duplicate check. The user can view these LTA in Temenos Payments Hub in appropriate file level enquiries.

## Qualifying LTA as Payment

Depending upon specific conditions under which the LTA is received, Temenos Payments Hub qualifies them as a payment, called as LTA Payment. The conditions to be evaluated (in order to consider an LTA as a payment and book them) are based on the values of the below mentioned attributes:

- Sending Institution Identification
- Receiving Institution Identification
- Participant Identification
- Account Identification
- Advice Type
- Transfer Type
- Local Instrument Proprietary
- Local Instrument Code
- CSM Status Code
- Debtor Agent
- Debtor Account
- Creditor Agent
- Creditor Account

The user can configure qualification criteria to determine whether the LTA must be considered as a payment or not based on the above attributes. If the user prefers to handle an LTA in non-STP mode, then user can form the qualification criteria for an LTA and configure it to be disqualified so that LTA can be manually processed from the repair queue.

Read [configuration](../../EMI_Integrations/C2B_Message_Exchange/Misc/Configuration.htm) for more details on configuring qualification criteria for LTA.

## Deriving Accounts for LTA Payment

If LTA is qualified as a payment, the notified account is debited or credited in the bank during processing of the LTA payment. The posting is mainly for liquidity management purposes, such that the Nostro balances are up-to-date with the balance or positions in the actual account in AHI. This enables the bank to perform efficient liquidity management functions.

LTA payment comprises a debit account and a credit account that represent accounts where the AHI affects the liquidity adjustments. Both these accounts are external accounts to the bank, hence Temenos Payments Hub resolves these accounts to an in-house Nostro or suspense account within the bank to perform necessary bookings.

## Handling LTA from Repair Queue

If the system is unable to process an LTA because of validation failure, then the payment is parked in repair queue.

LTA that failed to qualify as a payment, failed while resolving the account, failed duplicate check, or failed clearing specific validations, is available in repair queue for repairing by the bank user. In some cases, it can even be the user who prefers non-Straight Through Processing (STP) payment handling of a LTA (specific conditions are configured to disqualify the LTA). The user can search for LTA awaiting repair using dedicated repair enquiry in Temenos Payments Hub (Read for more details).

From the repair page, the user can either cancel or modify the LTA details. The user can modify the below fields in the LTA screen of Temenos Payments Hub during repair operation.

- *Value Date*
- *Debit Account*
- *Credit Account*

After repair and supervisor’s approval (if configured), the LTAs are moved back to processing starting from the LTA qualification activity.

The authoriser approves the above mentioned user performed actions.

When the user cancels the LTA, the payment reaches a final cancelled status on authorisation. When cancelling a payment, the user enters the reason for cancelling the payment.

When the user modifies the LTA, accept the warnings, and validates or submits the LTA, the system validates the LTA again to ensure that the functional errors do not arise again. After accepting the warning raised for a particular validation failure, the warnings do not raise again. After the operator repairs the payment, the operator can click *Validate* to validate the input.

## Viewing LTA through Enquiry

The user can view the LTA that clears file level validation and moves to Temenos Payments Hub, in dedicated enquiry. This enquiry enables the user to view LTA that are in various status such as, Completed, Repair and so on. The user can only view the details and cannot modify it. Read the Viewing LTA transaction in Temenos Payments Hub section in the Working with Liquidity Transfer Advices topic.

In this topic

- [Introduction to Liquidity Transfer Advice](#IntroductiontoLiquidityTransferAdvice)

- [Co-Management](#CoManagement)
- [Processing LTA at Temenos Payments Hub](#ProcessingLTAatTemenosPaymentsHub)
- [Qualifying LTA as Payment](#QualifyingLTAasPayment)
- [Deriving Accounts for LTA Payment](#DerivingAccountsforLTAPayment)
- [Handling LTA from Repair Queue](#HandlingLTAfromRepairQueue)
- [Viewing LTA through Enquiry](#ViewingLTAthroughEnquiry)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:21:21 PM IST