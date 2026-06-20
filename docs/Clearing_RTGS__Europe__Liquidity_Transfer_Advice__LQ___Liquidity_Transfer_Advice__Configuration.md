# Configuring Liquidity Transfer Advice

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Configuration.htm

---

2. [Payments](../../../../content/payments.html)

- Europe;)

Payments

# Configuring Liquidity Transfer Advice

Updated On 22 March 2025 |
 8 Min(s) read

Feedback
Summarize

Temenos Payments Hub determines whether the received LTA is a payment or not. After determining the LTA as a payment, it resolves the internal accounts based on the received external accounts.

## Configuring LTA to Qualify as Payment

To configure LTA to qualify as a payment, go to **Admin Menu** > **Payments** > **Liquidity Management** > **LTA Qualification.**



On the LTA Qualification List page, the user can perform the below actions:

- Click  to modify the existing record.
- Click  to view the existing records.
- Click  to reverse the entry.

To create a record, the user needs to establish a business rule with one or more of the below mentioned LTA attributes that meets the business requirement. The user can set the received LTA as a payment depending on the selected attributes.



The user can choose any of the below attributes to be considered for LTA payments:

| Fields | Descriptions |
| --- | --- |
| *Sender Institution Identification* | Indicates the ID of the institution sending the LTA. For example, BIC of the CSM |
| *Receiver Institution Identification* | Indicates the ID of the institution receiving the LTA. For example, BIC of the bank |
| *Participant Identification* | Indicates the ID of the participant whose liquidity position or balance is adjusted. In this case, it is the bank BIC (BIC as registered with the CSM) where it is a direct participant or liquidity serviced participant |
| *Ranking* | Determines the priority of selecting the record. It is based on ascending order. Rank 1 gets highest preference compared to Rank 999 |
| *Account Identification* | Indicates the account of the participant whose liquidity position or balance is adjusted. This can be a bank identifier or account. The bank account (held in CSM) is a direct participant or liquidity serviced participant |
| *Advice Type* | The user can decide if the LTA is for a debit operation or credit operation   - Debit indicator (DBIT) indicates debit on the account (found in the *Debtor Account* field) - Credit indicator (CRDT) indicates credit on the account (found in the *Credit Account* field) |
| *Transfer Type* | Determines the type of underlying transfer with respect to the received LTA. This varies with respect to each clearing |
| *CSM Status Code* | Indicates the status of the adjustments as recorded within the CSM system |
| *Local Instrument Proprietary* | The user can set the proprietary type of underlying LTA. The values change based on the clearing |
| *Debtor Agent* | Indicates the identifier of the agent who is getting debited. This can be CSM Identifier (BIC), the bank settlement BIC with the CSM, or liquidity provider’s settlement BIC depending upon whether LTA is a debit or credit operation |
| *Creditor Agent* | Indicates the identifier of the agent who is getting credited. This can be CSM Identifier (BIC) or the bank settlement BIC with the CSM or any liquidity provider’s settlement BIC, depending upon whether LTA is a credit or debit operation |
| *Debtor Account* | Indicates the account identifier of the debtor agent who is getting debited. This can be CSM account or the bank account with the CSM or any of the liquidity serviced participant’s account in case the bank provides the service, depending upon whether LTA is a debit or credit operation |
| *Creditor Account* | Indicates the account identifier of the creditor agent who is getting credited. This can be CSM account or the bank account with the CSM or any of the liquidity serviced participant’s account in case the bank provides the service, depending upon whether LTA is a credit or debit operation |
| *Local Instrument Code* | The user can give the value of clearing-specific codes as received |
| *LTA Payment* | The user can decide whether the LTA received is considered as a payment (if selected Y) or not (if selected N) based on the inputs given. If configured as ‘N’, then the system parks the LTA in the repair queue. |

Based on the above values and ranking, the system chooses the appropriate rule and based on that, it can determine whether to consider it as a payment or not.

## Configuring LTA to Resolve the Accounts

Once LTA is determined as a payment, Temenos Payments Hub resolves the LTA payment with internal accounts based on the account details received through LTA. The user can configure for both debit and credit accounts.

To resolve the accounts, go to **Admin Menu** > **Payments** > **Liquidity Management** > **Account Mapping.**



From the LTA Account Derivation List page, the user can perform the following actions:

- Click  to modify the existing record.
- Click  to view the existing record.
- Click  to reverse the entry.

To create a record, the user needs to establish a business rule with one or more of the following LTA attributes that meets the business requirement.



| Fields | Descriptions |
| --- | --- |
| *Institution Identification* | Indicates the ID of the institution sending the LTA |
| *Liquidity Transaction Type* | Indicates whether the configuration is for LTA or LTR |
| *Debit/Credit Operation* | Determines whether the account should be debited or credited   - Debit - The particular account needs to be debited - Credit - The particular account needs to be credited |
| *Advice Type* | Indicates whether the LTA is for a debit operation or credit operation   - Debit indicator (DBIT) indicates debit on the account (found in *Debtor Account* field) - Credit indicator (CRDT) indicates credit on the account (found in *Credit Account* field) |
| *External Account Identifier* | Indicates the account number received from LTA. It is the account number maintained at Account Holding Institutions (AHI) |
| *External Account Name* | Indicates the name of the account received from the LTA |
| *Counterparty Account* | Indicates the account in the counter leg of the LTA. Specifies the External Credit Account when the *Debit/Credit Operation* is Debit and External Debit Account when the *Debit/Credit Operation* is Credit. This field can be configured only when *Liquidity Transaction Type* is LTA |

Based on the above values, the system chooses the appropriate rule and considering that, it can determine the internal accounts available in the system.

| Fields | Descriptions |
| --- | --- |
| *Account Company* | The user can create LTA rules only for their own company, that is, the Temenos Transact company where they belong  The user’s company is defaulted in the field and cannot be modified |
| *Account Currency* | Indicates the currency of the resolved internal account. This is defaulted in the field and cannot be modified |
| *Internal Account* | Indicates the clearing or suspense account maintained internally. This account is resolved for the external account received |

The bank needs to configure suitable accounts in order to resolve the accounts based on the notification type.

If the bank gets multiple notifications from clearings, the user can use both LTA Qualification and LTA Account Mapping to qualify any one of them.

In case Temenos Payments Hub is configured as standalone, the bank user needs to configure the internal accounts in the PP.NON.CUSTOMER.ACCOUNTS table. This avoids external interfacing for validating the accounts. Read the Standalone guide for more information.

In this topic

- [Configuring Liquidity Transfer Advice](#ConfiguringLiquidityTransferAdvice)

- [Configuring LTA to Qualify as Payment](#ConfiguringLTAtoQualifyasPayment)
- [Configuring LTA to Resolve the Accounts](#ConfiguringLTAtoResolvetheAccounts)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:22:25 PM IST