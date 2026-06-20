# Introduction to FATF and WTR 2

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/FATF/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Temenos Payments Hub > FATF and WTR2 > Introduction

- Temenos Payments Hub;)
  - [Introduction](../../Payments_Hub_(PP)/Misc/Introduction.htm)
  - [Messaging Framework Messaging Framework](../../Payments_Hub_(PP)/MessagingFramework/Introduction.htm)
  - Clearing;)
  - Sanction Screening;)
  - Status Reporting;)
  - Cheque Clearing;)
  - Code Words;)
  - Direct Debits;)
  - International Payments (MT);)
  - Manual Repair;)
  - Business Dates;)
  - Posting;)
  - Fees and Billing;)
  - Funds Reservation;)
  - Warehousing;)
  - Book Transfer;)
  - Investigations and Enquiries;)
  - Routing and Settlement;)
  - Business Validations;)
  - Static Data;)
  - Standalone Payments;)
  - [Standalone Implementation Options Standalone Implementation Options](../../Payments_Hub_(PP)/Standalone_Implementation_Options/Standalone_Implementation_Options.htm)
  - Forex;)
  - Bulk Payments;)
  - Bank Condition;)
  - Client Condition;)
  - Product Determination;)
  - Housekeeping Functions;)
  - FATF and WTR2;)
    - [Introduction](../../Payments_Hub_(PP)/FATF/Introduction.htm)
    - [Configuration](../../Payments_Hub_(PP)/FATF/Configuration.htm)
    - [Working with](../../Payments_Hub_(PP)/FATF/Working_with.htm)
    - [Tasks](../../Payments_Hub_(PP)/FATF/Tasks.htm)
    - [Outputs](../../Payments_Hub_(PP)/FATF/Outputs.htm)
  - PSD2;)
  - SWIFT gpi;)
  - SWIFT Universal Confirmations;)
  - Instant Payments;)
  - Agency Banking;)
  - Returns and Reversal;)
  - Exceptions and Investigations;)
  - Clearing Status Report;)
  - Monitoring;)
  - Counterparty Risk;)

Payments

# Introduction to FATF and WTR 2

Updated On 22 March 2025 |
 6 Min(s) read

Feedback
Summarize

The Financial Action Task Force (FATF) recommendations are internationally endorsed global standards against money laundering and terrorist financing. They increase transparency and enable countries to successfully take action against illicit use of their financial system. FATF Special Recommendation (SR) VII governs the ordering party details that are sent as part of SWIFT customer transfers.

Latest FATF recommendations follow the obligations set out in the relevant United Nations Security Council resolutions.

FATF validations are performed for the following payment types:

- International payments (SWIFT)
- Credit Transfer (CT) and Direct Debit (DD) settled through local clearing
- Outward and book transfers
- Child transactions within a batch

FATF validations are not performed on returns, reversals, and refunds.

To enable FATF validation, Go to **Admin Menu** > **Payments** > **Payments Hub** > **Bank System Administration** > **Local Clearing** > **Clearing Setting** and set the *Clearing Transaction Type* field as mentioned below:

| Scenario | Value |
| --- | --- |
| For inward credit transfers or initiations | Set as CT or Blank. |
| For direct debits | Set as DD. |

FATF based on the recommendation 16 can be classified into two sections depending on the region:

- Global Regulation
- European Regulation

European Regulations adopt the WTR 2 regulations.

## Global Regulation

FATF regulation requires the payer PSP to ensure ordering party details (Name, Account number/ identified & complete address) are captured and forwarded as part of payment message while sending international or domestic payments. Similarly, payee PSPs have an obligation to ensure the availability of details mentioned below:

Payer (person holding the account from which the payment is made) Information:

- Name of the payer
- Payers payment account number
- Payers address

Payee (intended recipient of the funds) Information:

- Name of the payee
- Payee account number

## European Regulation

According to the EU Regulations, parties (Ordering and Beneficiary party) can have their account with a bank in EEA or either one of the parties can hold their accounts out of EEA.

- If both the parties hold the account within EEA, then only the Account Number and Name of the ordering party are sufficient
- If only one party has their account in EEA, then Account Number, Name, and Address details of the ordering party are mandatory.

For parties within EEA region, PSP checks the accuracy of details specific to only ‘Name of Payer’ and ‘Payer’s Account Number’.

|  | Payer and Payee within EEA | Payment from EEA to non-EEA entity | | Payment from non-EEA to EEA entity | |
| --- | --- | --- | --- | --- | --- |
| > EUR 0,00 | < EUR 1000 | > EUR 1000 | < EUR 1000 | > EUR 1000 |
| Payer's Name | - | x | x | x | x |
| Payer's Account Number | x | x | x | x | x |
| Payer's Address | - | - | x | x | x |
| Payee's Name | - | - | x | x | x |
| Payee's Account Number | x | x | x | x | x |

## Wire Transfer Regulation 2 (WTR 2)

Wire Transfer Regulations 2(WTR 2) is enacted as part of the European Union (EU) Anti-Money Laundering (AML) and counter terrorism measures and perform alongside the various other AML and Counter- Terrorism Financing (CTF) regulations. This came into existence as a direct consequence of FATF SR VII.

EU should ensure that the International Standards on Combating Money Laundering and the Financing of Terrorism and Proliferation adopted by FATF in Recommendation 16 on wire transfers are implemented uniformly throughout the Union.

WTR 2 regulation have rules on the information of payers and payees, accompanying transfers of funds (in any currency). This helps in preventing, detecting, and investigating the money laundering and terrorist financing, where one of the Payment Service Providers (PSP) (involved in the transfer of funds) is established in the Union.

WTR 2 mandates Payee PSP to effectively monitor Payer details in inward remittances when Payer PSP is established,

- within European Economic Area (EEA)
- outside European Economic Area (non-EEA)

## Performing Beneficiary Name Comparison on Inward Payments

WTR 2 broadens the regulatory requirements around the information related to payers and payees that must accompany a transfer of funds, sent or received in any currency, when either the payer’s or payee’s PSP, or an intermediary PSP, is established in the EU or EEA.

Article 7 of WTR 2 recommends the payee PSPs to perform the following validations:

- Detect whether regulatory required information is transmitted in the designated fields
- Verify the accuracy of the information received on the payee

Temenos Payments Hub supports Article 7 of WTR 2 for inward payments by performing optional Name-Comparsion check for both European and Global regulations:

- Match beneficiary’s name specified in the inward payment message against customer name stored in the Customer & Account statis tables
- Convert both beneficiary names (received from the message and retrieved from the system) to a single case (upper or lower)

If both matches, the payment is processed successfully. Read [Enable Name Comparison Check](Configuration.htm#Enabling_Name_Comparison_Check) for more information.

The name comparison feature is basic and linked with FATF/WTR2 configuration that cannot cater to complex scenarios. To support such complexities, TPH offers enhanced Beneficiary Name Comparison (BNC) feature that allows the users to define invoke name check criteria.

Read [Introduction to Temenos Payments Hub](../Misc/Introduction.htm) to understand more about the enhanced name comparison feature;

In this topic

- [Introduction to FATF and WTR 2](#IntroductiontoFATFandWTR2)

- [Global Regulation](#GlobalRegulation)
- [European Regulation](#EuropeanRegulation)
- [Wire Transfer Regulation 2 (WTR 2)](#WireTransferRegulation2WTR2)
- [Performing Beneficiary Name Comparison on Inward Payments](#PerformingBeneficiaryNameComparisononInwardPayments)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 2:55:39 PM IST