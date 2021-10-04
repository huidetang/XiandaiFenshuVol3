module ReVIEW
    module HTMLBuilderOverride
      def inline_bib(id)
        %Q(<a href="#{@book.bib_file.gsub(/\.re\Z/, ".#{@book.config['htmlext']}")}#bib-#{normalize_id(id)}">[<span class="tcy">#{@chapter.bibpaper(id).number}</span>]</a>)
      rescue KeyError
        app_error "unknown bib: #{id}"
      end

      def bibpaper_header(id, caption)
        print %Q(<a id="bib-#{normalize_id(id)}">)
        print %Q([<span class="tcy">#{@chapter.bibpaper(id).number}</span>])
        print '</a>'
        puts " #{compile_inline(caption)}"
      end
    end

    module LATEXBuilderOverride
      def bibpaper(lines, id, caption)
        puts %Q(\\bibitem{bib:#{id}} #{split_paragraph(lines).join("\n\n")})
      end
    end
  
    class HTMLBuilder
      prepend HTMLBuilderOverride
    end

    class LATEXBuilder
      prepend LATEXBuilderOverride
    end
  end