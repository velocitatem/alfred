(defun function-for-financial-template ()
  (concat ledger-date-string-today " *%^{Event} \n\t" "Expenses:%^{type} \t\t %^{amount}\n\tAssets:Budget:%<%B>" ))

(setq org-capture-templates  '(("f" "Add a financial expense" plain
                                (file "/home/velo/Documents/Me/Finance/my.ledger")
                                (function function-for-financial-template))
                               ))
