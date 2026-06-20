# Introduction to Payments Repair

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/VS/Payments_Repair/Payments_Repair/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Payments Repair > Introduction

- Payments Repair;)
  - [Introduction](../../Payments_Repair/Payments_Repair/Introduction.htm)
  - [Configuration](../../Payments_Repair/Payments_Repair/Configuration.htm)
  - [Working with](../../Payments_Repair/Payments_Repair/Working_with.htm)
  - [Tasks](../../Payments_Repair/Payments_Repair/Tasks.htm)
  - [Outputs](../../Payments_Repair/Payments_Repair/Outputs.htm)

Payments

# Introduction to Payments Repair

Updated On 22 March 2025 |
 6 Min(s) read

Feedback
Summarize

Temenos Payments Hub Repair is an automated repair tool that repair messages and payments without manual intervention. It changes free text to IDs that can be recognised by the payment system such as, Temenos Payments Hub (TPH).

If the bank name and address are changed to BIC code and/or National ID, the Payments Repair reformats the account number to the correct format.

There are two versions of Temenos Payments Hub Repair available for the user.

- Standard version

- Has limited reference data.
- Enriches the payment messages based on tables filled by the customer.

- Enterprise version

- Uses both SWIFT BankDataPlus database and the tables filled by the customer.
- Fully enables the lexical Repair capabilities of the tool using Bank, City, and Country lexicons (defining synonyms).

[](#)[Input and Output Message](#)

TPH (or any other payment system) forwards a set of fields to Payments Repair for repairing messages.

The *Currency* and *Transaction Amount* fields are not repaired by Payments Repair.

Given below are the fields that are forwarded to Payments Repair from TPH, XML, or MT message:

| Field Neutral Format | ISO Party/Agent (Functional Name) | MT Party | Party Received in TPH Format |
| --- | --- | --- | --- |
| *FE\_SENDER* | Instructing Agent | Sender | Debit Party Role SENDER |
| *FE\_INDAGT* | Instructed Agent | Receiver | Credit Party Role INDAGT |
| *FE\_ORDPTY* | Debtor | Ordering Party | Debit Party Role ORDPTY |
| *FE\_INSPTY* | Initiating Party | Instructing Party | Debit Party Role INSPTY |
| *FE\_ORDINS* | Debtor Agent | Ordering Institution | Debit Party Role ORDINS |
| *FE\_SNDCBK* | Instructing Reimbursement Agent | Sender’s Correspondent | Debit Party Role SNDCBK |
| *FE\_RCVCBK* | Instructed Reimbursement Agent | Receiver’s Correspondent | Debit Party Role RCVCBK |
| *FE\_TRMINS* | Third Reimbursement Agent | Third reimbursement Party | Debit Party Role TRMINS |
| *FE\_PRVINS* | Previous Instructing Agent 1 | NA | Debit Party Role PRVINS |
| *FE\_PRVIN2* | Previous Instructing Agent2 | NA | Debit Party Role PRVIN2 |
| *FE\_PRVIN3* | Previous Instructing Agent3 | NA | Debit Party Role PRVIN3 |
| *FE\_INTINS* | Intermediary Agent 1 | Intermediary Institution | Credit Party Role INTINS |
| *FE\_INTIN2* | Intermediary Agent2 | NA | Credit Party Role INTIN2 |
| *FE\_INTIN3* | Intermediary Agent3 | NA | Credit Party Role INTIN3 |
| *FE\_ACWINS* | Creditor Agent | Account With Institution | Credit Party Role ACWINS |
| *FE\_BENINS* | Creditor (pacs.009) | Beneficiary Institution (58) | Credit Party Role BENINS |
| *FE\_BENFCY* | Creditor (pacs.008) | Beneficiary Customer (59) | Credit Party Role BENFCY |
| *FE\_ULTDBT* | Ultimate Debtor | NA | Debit Party Role ULTDBT |
| *FE\_ULTCDT* | Ultimate Creditor | NA | Credit Party Role ULTCDT |
| *FE\_CHGAGT* | Charge Agent | NA | Credit Party Role CHGAGT or Debit Party Role CHGAGT |
| *FE\_FWDAGT* | Forwarding Agent | Sending Institution (51A) | Debit Party Role FWDAGT |
| *SQ\_REMITINFO* | Unstructured Remittance information | Reason of Payment | Additional Information |
| *SQ\_BKTOBKINFO* | See Bank to Bank Information | See Bank to Bank Information | Read the [Bank to Bank Information](#B2B_Info) section. |
| *SQ\_INSTRCAGT* | Instruction for Creditor Agent | NA | Read the [Bank to Bank Information](#B2B_Info) section. |
| *SQ\_INSTRNAGT* | Instruction for Next Agent | NA | Read the [Bank to Bank Information](#B2B_Info) section. |
| *SQ\_SUPPLEMENTARYDAT*A | Supplementary Data Place and Name | NA | NA |

Given below are the other fields used for configuring payments repair:

| Field Name | ISO Party or Agent | MT Party | TPH |
| --- | --- | --- | --- |
| *Message Type* | pacs.009, pacs.008 or pain.001 | 103, 202, or 101 | Message Format:  pacs.009, pacs.008, pain.001, 103, 202, 101, 200, 205 and so on  Any other message types as from the PAYMENT.ORDER application |
| *Message Identifier* | MessageIdentification | NA | Message ID |
| *Payment Information ID* | PaymentInformationIdentification | NA | NA |
| *Instruction ID* | InstructionIdentification | Field 20 | InstructionIdentification |
| *End to end ID or Related Reference* | EndToEndIdentification | NA | EndToEndIdentification |
| *Transaction Identifier* | TransactionIdentification | NA | FTnumber |
| *Unique end to end Transaction Reference* | UETR | UETR | Not mapped |
| *Clearing System Reference* | ClearingSystemReference | NA | NA |
| *Instruction Priority* | InstructionPriority | From Header block 2: If last character is N map NORM, If last character is U map HIGH | Instruction Priority |
| *Clearing Channel* | ClearingChannel | NA | NA |
| *Settlement Amount* | InterbankSettlementAmount | Interbank Settled Amount (32A) | Transaction Amount |
| *Settlement Currency* | InterbankSettlementAmount or EquivalentAmount/CurrencyOfTransfer | Interbank Settled Amount (32A) | Transaction Currency Code |
| *Instructed Amount* | InstructedAmount or EquivalentAmount | Instructed Amount (33B) | Instructed Amount |
| *Instructed Currency* | InstructedAmount or EquivalentAmount | Instructed Amount (33B) | Instructed Currency |
| *Charge Bearer* | ChargeBearer | Details of Charges (71A) | Not mapped |
| *Initiation Source Name* (Application Name) | InitiationSource/Name | Header block 3 content after field 103, if not present: 'SWIFT' | NA |
| *Office* | Field Office in the Json | Field Office in the Json | Company ID |
| *Payment Source* | Field Source in the Json | Field Source in the Json | Originating Source |
| *Channel* | Field Channel in the Json | Field Channel in the Json | Originating Channel |
| *Message Format* | NA | NA | TPH |

[](#)[Bank to Bank Information](#)

If the system checks the bank to bank information in the tables, the next information from the message is checked against the table.

With the standard rules, bank to bank information is not changed.

| Field in table | Used from MT Message (and TPH) | Used from ISO Message (and TPH) |
| --- | --- | --- |
| Bank to Bank information | Mapped from MT message from field 72. TPH if INFORMATIONCODE is INSSDR and INSTRUCTIONCODE not one of TXPURPCD /TXPURPPY/STTLMTPY | Mapped from ISO and TPH SQ\_INSTRCAGT and SQ\_INSTRNAGT |
| Bank to Bank information | /REC/VALUE or VALUE) | /PHOB/VALUE or VALUE  First Instruction for Next agent is used, if there are no instructions present (anymore) the instructions for creditor agent is checked. |

[Available Rules](#)

Read the [Working with Payments Repair](Working_with.htm) topic for information on the rules and configuring the tables to use the rules.

In this topic

- [Introduction to Payments Repair](#IntroductiontoPaymentsRepair)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:09:48 PM IST